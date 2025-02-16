from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.model_handler import get_model
from services.summary_pipeline import process_text


router = APIRouter(prefix="/llm", tags=["llm"])

class QuestionRequest(BaseModel):
    question: str

@router.post("/summarize/")
def summarize_text():
    summary = process_text("data/text.txt")
    return {"summary": summary}

@router.post("/ask/")
def ask_model(request: QuestionRequest):
    model = get_model()

    try:
        response = model.invoke(request.question)
        return {"question": request.question, "answer": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
