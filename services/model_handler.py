import os
from langchain_community.llms import Ollama, OpenAI


def get_model():
    model_type = os.getenv("MODEL_TYPE", "ollama")

    if model_type == "openai":
        return OpenAI(model_name="gpt-4", openai_api_key=os.getenv("OPENAI_API_KEY"))
    else:
        return Ollama(model=os.getenv("OLLAMA_MODEL"))
