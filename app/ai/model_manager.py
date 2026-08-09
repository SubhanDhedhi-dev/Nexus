from app.ai.provider_manager import ProviderManager


class ModelManager:

    def __init__(self):
        self.provider_manager = ProviderManager()

    def generate(self, prompt: str) -> str:
        return self.provider_manager.generate(prompt)

    def set_provider(self, provider_name: str):
        self.provider_manager.set_provider(provider_name)

    def get_provider(self) -> str:
        return self.provider_manager.active_provider

    def list_providers(self):
        return self.provider_manager.list_providers()