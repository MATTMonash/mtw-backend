from typing import Any

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama

from app.llms.local_llms import get_local_ollama_models

from app.config import settings


class LLMManager:
    """Manages multiple LLM providers"""

    def __init__(self):
        self._models: dict[str, Any] = {}
        self._initialise_models()

    def _initialise_models(self):
        """Initialise available models based on API keys and local installation"""
        # Google
        if settings.google_api_key:
            self._models["google"] = ChatGoogleGenerativeAI(
                model="gemini-2.5-flash",
                temperature=0,
                max_tokens=None,
                timeout=None,
                max_retries=2,
                google_api_key=settings.google_api_key,
            )

        # Local Ollama LLMs
        local_models = get_local_ollama_models()
        for local_model in local_models:
            self._models[local_model] = ChatOllama(
                model=local_model,
                temperature=0
            )


    def get_llm(self, model_name: str | None = None):
        """Get LLM by name or return default"""
        if model_name and model_name in self._models:
            return self._models[model_name]
        return next(iter(self._models.values()))


llm_manager = LLMManager()
