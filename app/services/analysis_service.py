import random

from app.schemas.image import AnalyzeResponse

SKIN_TYPES = ["Oily", "Dry", "Combination", "Normal", "Sensitive"]

POSSIBLE_ISSUES = [
    "Hyperpigmentation",
    "Acne",
    "Fine Lines",
    "Dark Circles",
    "Redness",
    "Uneven Texture",
    "Dehydration",
]


def analyze_image(image_id: str) -> AnalyzeResponse:
    skin_type = random.choice(SKIN_TYPES)
    num_issues = random.randint(0, 3)
    issues = random.sample(POSSIBLE_ISSUES, num_issues)
    confidence = round(random.uniform(0.70, 0.99), 2)

    return AnalyzeResponse(
        image_id=image_id,
        skin_type=skin_type,
        issues=issues,
        confidence=confidence,
    )
