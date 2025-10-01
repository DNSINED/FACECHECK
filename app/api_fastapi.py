from __future__ import annotations
from typing import Any, Dict, Tuple
import base64
import io

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from PIL import Image

app = FastAPI(title="FakeCheck API (stub)")


class AnalyzeRequest(BaseModel):
    image_b64: str


def mock_infer(img: Image.Image) -> Tuple[str, float, Tuple[float, float], bool]:
    return "Inconclusive", 0.50, (0.45, 0.55), False


@app.post("/analyze")
def analyze(req: AnalyzeRequest) -> Dict[str, Any]:
    try:
        img_bytes = base64.b64decode(req.image_b64)
        img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
    except Exception as e:  # noqa: BLE001
        raise HTTPException(status_code=400, detail=f"Invalid image: {e}")
    verdict, score, band, unstable = mock_infer(img)
    return {"verdict": verdict, "score": score, "band": list(band), "unstable": unstable}
