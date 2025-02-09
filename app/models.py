from pydantic import BaseModel

# Request models
class TextCompletionRequest(BaseModel):
    prompt: str
    max_length: int = 50

class TextSummarizationRequest(BaseModel):
    text: str
    max_length: int = 130
    min_length: int = 30

# Response models
class TextCompletionResponse(BaseModel):
    completed_text: str

class TextSummarizationResponse(BaseModel):
    summary: str