import logging

from fastapi import APIRouter, File, HTTPException, UploadFile, status

from app.schemas.image import AnalyzeRequest, AnalyzeResponse, UploadResponse
from app.services.analysis_service import analyze_image
from app.services.storage_service import get_cached_result, store_result
from app.services.upload_service import save_uploaded_file
from app.utils.file_utils import image_exists

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post(
    "/upload", response_model=UploadResponse, status_code=status.HTTP_201_CREATED
)
async def upload_image(file: UploadFile = File(...)):
    image_id = await save_uploaded_file(file)
    logger.info(f"Image uploaded successfully: {image_id}")
    return UploadResponse(image_id=image_id)


@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze(request: AnalyzeRequest):
    if not image_exists(request.image_id):
        logger.warning(f"Analysis requested for unknown image: {request.image_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Image not found: {request.image_id}",
        )

    cached = get_cached_result(request.image_id)
    if cached:
        logger.info(f"Returning cached result for image: {request.image_id}")
        return cached

    result = analyze_image(request.image_id)
    store_result(result)
    logger.info(f"Analysis completed for image: {request.image_id}")
    return result
