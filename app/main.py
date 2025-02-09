from fastapi import FastAPI, HTTPException
from .models import TextCompletionRequest, TextSummarizationRequest
from .utils import complete_text, summarize_text, load_text_generator, load_summarizer

app = FastAPI()

# Load models
text_generator = load_text_generator()
summarizer = load_summarizer()

@app.post("/complete")
async def text_completion(request: TextCompletionRequest):
    try:
        completed_text = complete_text(text_generator, request.prompt, request.max_length)
        return {"completed_text": completed_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/summarize")
async def text_summarization(request: TextSummarizationRequest):
    try:
        summary = summarize_text(summarizer, request.text, request.max_length, request.min_length)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/health")
async def health_check():
    return {"status": "ok"}