from fastapi import FastAPI
from services.summary_pipeline import process_text

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API for text summarization is running"}

@app.post("/summarize/")
def summarize_text():
    summary = process_text("data/input.txt")
    return {"summary": summary}
