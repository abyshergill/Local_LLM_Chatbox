import requests

def get_local_llm_models():
    """Attempt to detect local LLM models from Ollama."""
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=2)
        response.raise_for_status()
        data = response.json()
        return [model["name"] for model in data.get("models", [])]
    except requests.RequestException:
        print("Warning: Could not connect to Ollama server at http://localhost:11434. Please ensure Ollama is running.")
        return []
