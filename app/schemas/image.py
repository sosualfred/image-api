from pydantic import BaseModel


class UploadResponse(BaseModel):
    image_id: str


class AnalyzeRequest(BaseModel):
    image_id: str


class AnalyzeResponse(BaseModel):
    image_id: str
    skin_type: str
    issues: list[str]
    confidence: float


class ErrorResponse(BaseModel):
    detail: str
