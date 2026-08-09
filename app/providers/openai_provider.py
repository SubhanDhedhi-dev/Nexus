import os

from app.providers.base_provider import BaseProvider


class OpenAIProvider(BaseProvider):
    """
    OpenAI provider for Nexus.

    The API key is read from the OPENAI_API_KEY
    environment variable.
    """

    def __init__(self, model: str = "gpt-4o-mini"):
        self.name = "OpenAI"
        self.model = model
        self.client = None

        api_key = os.getenv("OPENAI_API_KEY")

        if api_key:
            try:
                from openai import OpenAI

                self.client = OpenAI(
                    api_key=api_key
                )

            except ImportError:
                print(
                    "[OpenAI] OpenAI package is not installed."
                )

    def is_available(self) -> bool:
        """
        OpenAI is available only when an API key
        and the OpenAI package are available.
        """

        return self.client is not None

    def generate(self, prompt: str) -> str:
        """
        Send a prompt to OpenAI.
        """

        if not self.is_available():
            raise RuntimeError(
                "OpenAI provider is not available. "
                "Check OPENAI_API_KEY and the openai package."
            )

        print(
            f"[OpenAI] Generating response "
            f"with {self.model}..."
        )

        response = self.client.responses.create(
            model=self.model,
            input=prompt
        )

        return response.output_text