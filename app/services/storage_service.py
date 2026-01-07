import json
from pathlib import Path

from app.schemas.image import AnalyzeResponse

RESULTS_FILE = Path("analysis_results.json")

_cache: dict[str, dict] = {}


def _load_cache() -> None:
    global _cache
    if RESULTS_FILE.exists():
        with open(RESULTS_FILE, "r") as f:
            _cache = json.load(f)


def _save_cache() -> None:
    with open(RESULTS_FILE, "w") as f:
        json.dump(_cache, f, indent=2)


_load_cache()


def get_cached_result(image_id: str) -> AnalyzeResponse | None:
    if image_id in _cache:
        return AnalyzeResponse(**_cache[image_id])
    return None


def store_result(result: AnalyzeResponse) -> None:
    _cache[result.image_id] = result.model_dump()
    _save_cache()
