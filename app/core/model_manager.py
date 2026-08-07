class ModelManager:
    """
    Handles all AI model interactions.

    Future Responsibilities:
    - OpenAI
    - Ollama
    - Gemini
    - Claude
    - LM Studio
    - Model selection
    - Token tracking
    - Cost tracking
    """

    def __init__(self):
        self.active_model = "Fake AI"

    def generate(self, prompt: str) -> str:

        print(f"\n[Model Manager] Using {self.active_model}")

        return (
            "This is a fake AI response.\n"
            "Later this will come from GPT or Ollama."
        )