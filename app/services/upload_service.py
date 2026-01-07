import logging

from fastapi import HTTPException, UploadFile, status

from app.config import ALLOWED_EXTENSIONS, MAX_FILE_SIZE, UPLOAD_DIR
from app.utils.file_utils import generate_image_id

logger = logging.getLogger(__name__)


def validate_file_type(content_type: str | None) -> None:
    if content_type not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file type. Allowed types: JPEG, PNG",
        )


def validate_file_size(size: int) -> None:
    if size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="File too large. Maximum size: 5MB",
        )


async def save_uploaded_file(file: UploadFile) -> str:
    content = await file.read()

    validate_file_type(file.content_type)
    validate_file_size(len(content))

    image_id = generate_image_id()
    extension = "jpg" if file.content_type == "image/jpeg" else "png"
    file_path = UPLOAD_DIR / f"{image_id}.{extension}"

    with open(file_path, "wb") as f:
        f.write(content)

    logger.info(f"Saved image: {image_id}")
    return image_id
