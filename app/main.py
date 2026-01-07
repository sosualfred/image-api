import logging

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.routes.image import router as image_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Image Analysis API",
    description="API for uploading and analyzing images",
    version="1.0.0",
)

app.include_router(image_router)


@app.get("/")
async def root():
    return {"message": "Image Analysis API", "version": "1.0.0"}


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": "An unexpected error occurred"},
    )
