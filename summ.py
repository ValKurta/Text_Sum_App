import requests
import json

OLLAMA_URL = "http://localhost:9117/api/chat"
model = "openhermes:latest"
file_path = "data/text.txt"

def generate_news_title(model_name, file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    prompt = f"Generate a short and concise headline for the following news article. Keep it brief and to the point:\n\n{text}"

    payload = {
        "model": model_name,
        "messages": [{"role": "user", "content": prompt}],
        #"max_tokens": 50
    }

    response = requests.post(OLLAMA_URL, json=payload, stream=True)

    full_response = ""

    for line in response.iter_lines():
        if line:
            try:
                data = json.loads(line.decode("utf-8"))

                if "message" in data and "content" in data["message"]:
                    full_response += data["message"]["content"].strip() + " "

            except json.JSONDecodeError as e:
                print(f"failed JSON: {e}")

    return full_response


print("title", generate_news_title(model, file_path))
