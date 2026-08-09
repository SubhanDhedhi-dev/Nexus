from app.providers.base_provider import BaseProvider


class FakeProvider(BaseProvider):

    def __init__(self):
        self.name = "Fake AI"

    def generate(self, prompt: str) -> str:

        print("[Fake AI] Generating response...")

        return (
            "This is a fake AI response.\n"
            "The real AI provider will be connected later."
        )

    def is_available(self) -> bool:
        return True