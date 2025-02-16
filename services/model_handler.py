import os
from langchain_ollama.llms import OllamaLLM

def get_model():
    model_type = os.getenv("MODEL_TYPE", "ollama")

    if model_type == "openai":
        from langchain_openai import OpenAI
        return OpenAI(model_name="gpt-4", openai_api_key=os.getenv("OPENAI_API_KEY"))
    else:
        return OllamaLLM(model=os.getenv("OLLAMA_MODEL"))
