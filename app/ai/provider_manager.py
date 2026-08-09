import os
from importlib.util import find_spec
from importlib import import_module


class ProviderManager:
    """
    Detects, selects, and communicates with AI providers.
    """

    def __init__(self):

        self.providers = {
            "fake": "app.providers.fake_provider",
            "openai": "app.providers.openai_provider",
            "ollama": "app.providers.ollama_provider",
            "claude": "app.providers.claude_provider",
            "gemini": "app.providers.gemini_provider",
        }

        self.available_providers = []

        self.detect_providers()

    # --------------------------------------------------
    # PROVIDER DETECTION
    # --------------------------------------------------

    def detect_providers(self):

        print(
            f"All providers: {list(self.providers.keys())}"
        )

        # Fake provider is always available.
        self.available_providers.append("fake")

        # OpenAI
        if os.getenv("OPENAI_API_KEY"):
            self.available_providers.append("openai")

        # Ollama
        if self._module_exists("ollama"):
            self.available_providers.append("ollama")

        # Claude
        if os.getenv("ANTHROPIC_API_KEY"):
            self.available_providers.append("claude")

        # Gemini
        if os.getenv("GEMINI_API_KEY"):
            self.available_providers.append("gemini")

        print(
            f"Available providers: "
            f"{self.available_providers}"
        )

    @staticmethod
    def _module_exists(module_name):

        try:
            return find_spec(module_name) is not None

        except (
            ImportError,
            ModuleNotFoundError,
            ValueError,
        ):
            return False

    # --------------------------------------------------
    # PROVIDER INFORMATION
    # --------------------------------------------------

    def get_available_providers(self):

        return self.available_providers.copy()

    def is_available(self, provider_name):

        return provider_name in self.available_providers

    # --------------------------------------------------
    # PROVIDER LOADING
    # --------------------------------------------------

    def get_provider(self, provider_name):

        if provider_name not in self.providers:
            raise ValueError(
                f"Unknown provider: {provider_name}"
            )

        if not self.is_available(provider_name):
            raise RuntimeError(
                f"Provider '{provider_name}' "
                f"is not available."
            )

        module_path = self.providers[provider_name]

        module = import_module(module_path)

        # Map provider names to their actual class names.
        provider_classes = {
            "fake": "FakeProvider",
            "openai": "OpenAIProvider",
            "ollama": "OllamaProvider",
            "claude": "ClaudeProvider",
            "gemini": "GeminiProvider",
        }

        class_name = provider_classes.get(provider_name)

        if not class_name:
            raise AttributeError(
                f"No provider class configured "
                f"for '{provider_name}'."
            )

        if not hasattr(module, class_name):
            raise AttributeError(
                f"Provider module '{module_path}' "
                f"does not contain '{class_name}'."
            )

        provider_class = getattr(module, class_name)

        return provider_class()

    # --------------------------------------------------
    # GENERATE
    # --------------------------------------------------

    def generate(self, prompt):

        provider_name = "fake"

        print(
            f"[Provider Manager] "
            f"Using provider: {provider_name}"
        )

        provider = self.get_provider(provider_name)

        return provider.generate(prompt)