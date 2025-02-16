import requests
import ollama
import json

OLLAMA_URL = "http://localhost:9117/api/chat"

print("Ollama import is working")

payload = {
    "model": "openhermes:latest",
    "messages": [{"role": "user", "content": "good evening, how are you? please respond in 3 words"}]
}
response = requests.post(OLLAMA_URL, json=payload, stream=True)

full_response = ""

for line in response.iter_lines():
    if line:
        try:
            data = json.loads(line.decode("utf-8"))

            if "message" in data and "content" in data["message"]:
                full_response += data["message"]["content"]

        except json.JSONDecodeError as e:
            print(f"Ошибка обработки JSON: {e}")

print(full_response)

