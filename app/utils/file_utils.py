import uuid
from pathlib import Path

from app.config import UPLOAD_DIR


def generate_image_id() -> str:
    return uuid.uuid4().hex[:12]


def get_image_path(image_id: str) -> Path | None:
    for file in UPLOAD_DIR.iterdir():
        if file.stem == image_id:
            return file
    return None


def image_exists(image_id: str) -> bool:
    return get_image_path(image_id) is not None
