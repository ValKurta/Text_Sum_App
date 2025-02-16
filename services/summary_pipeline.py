from services.text_processing import split_text
from services.model_handler import get_model


def process_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    chunks = split_text(text)
    model = get_model()

    summaries = [model.invoke(chunk) for chunk in chunks]

    final_summary = model.invoke("\n".join(summaries))
    return final_summary
