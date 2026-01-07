from pathlib import Path

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

ALLOWED_EXTENSIONS = {"image/jpeg", "image/png"}
MAX_FILE_SIZE = 5 * 1024 * 1024
