import json
import urllib.error
import urllib.request

from app.providers.base_provider import BaseProvider


class OllamaProvider(BaseProvider):
    """
    Local Ollama provider.

    Ollama normally runs on:
    http://localhost:11434
    """

    def __init__(
        self,
        model: str = "llama3.2",
        host: str = "http://localhost:11434"
    ):
        self.name = "Ollama"
        self.model = model
        self.host = host.rstrip("/")

    def is_available(self) -> bool:
        """
        Check whether Ollama is running.
        """

        try:
            request = urllib.request.Request(
                f"{self.host}/api/tags",
                method="GET"
            )

            with urllib.request.urlopen(
                request,
                timeout=2
            ):
                return True

        except (
            urllib.error.URLError,
            TimeoutError,
            ConnectionError
        ):
            return False

    def generate(self, prompt: str) -> str:
        """
        Send a prompt to the local Ollama server.
        """

        if not self.is_available():
            raise RuntimeError(
                "Ollama is not running or is unavailable."
            )

        print(
            f"[Ollama] Generating response "
            f"with {self.model}..."
        )

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        data = json.dumps(payload).encode("utf-8")

        request = urllib.request.Request(
            f"{self.host}/api/generate",
            data=data,
            headers={
                "Content-Type": "application/json"
            },
            method="POST"
        )

        try:
            with urllib.request.urlopen(
                request,
                timeout=120
            ) as response:

                result = json.loads(
                    response.read().decode("utf-8")
                )

            return result.get(
                "response",
                ""
            )

        except urllib.error.URLError as error:
            raise RuntimeError(
                f"Ollama request failed: {error}"
            ) from error