from fastapi import FastAPI
from services.summary_pipeline import process_text
from routes import api_llm

app = FastAPI()

app.include_router(api_llm.router)

@app.get("/")
def read_root():
    return {"message": "API for text summarization is running"}
