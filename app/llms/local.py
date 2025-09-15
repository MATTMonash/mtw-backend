"""
Retrieves a list of locally installed LLMs
"""

import requests

from app.config import settings

OLLAMA_API_URL = settings.ollama_api_url


def get_local_ollama_models() -> list[str]:
    """
    Fetch the list of locally installed Ollama model names.

    Returns:
        A list of strings with the names of installed models.
        Returns an empty list if an error occurs or no models found.
    """
    try:
        response = requests.get(OLLAMA_API_URL, timeout=3)
        response.raise_for_status()
        data = response.json()
        return [model["name"] for model in data.get("models", [])]
    except requests.exceptions.RequestException as e:
        print(f"Could not fetch locally installed Ollama models: {e}")
        return []


# if __name__ == "__main__":
#     models = get_local_ollama_models()
#     if models:
#         print("Available Ollama models:")
#         for model in models:
#             print(f"- {model}")
#     else:
#         print("No models could be found (or Ollama is not running).")
