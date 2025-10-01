from __future__ import annotations
from typing import Dict, List
import json
from pathlib import Path
from PIL import Image, JpegImagePlugin
import piexif


def extract_exif(path: str) -> Dict:

    try:
        exif_dict = piexif.load(path)
        make = exif_dict.get("0th", {}).get(piexif.ImageIFD.Make, b"").decode(errors="ignore") or None
        model = exif_dict.get("0th", {}).get(piexif.ImageIFD.Model, b"").decode(errors="ignore") or None
        return {"exif_present": bool(exif_dict and (make or model)), "camera_make": make, "camera_model": model}
    except Exception:
        return {"exif_present": False, "camera_make": None, "camera_model": None}


def read_qtables(path: str) -> Dict[int, List[int]]:
    try:
        with Image.open(path) as im:
            if not isinstance(im, JpegImagePlugin.JpegImageFile):
                return {}
            q = getattr(im, "quantization", None)
            # Pillow returns {table_id: [..coeffs..]}
            return {int(k): list(map(int, v)) for k, v in (q or {}).items()}
    except Exception:
        return {}


def _flatten_tables(qtables: Dict[int, List[int]]) -> List[int]:
    flat: List[int] = []
    for k in sorted(qtables.keys()):
        flat.extend(qtables[k])
    return flat


def qt_match_score(qtables: Dict[int, List[int]], profiles_path: str) -> float:
    if not qtables:
        return 0.0
    flat = _flatten_tables(qtables)
    if not flat:
        return 0.0

    try:
        profiles = json.loads(Path(profiles_path).read_text()).get("profiles", [])
    except Exception:
        return 0.0

    # Compare to each profile (truncate to min length)
    def score_one(ref: List[int]) -> float:
        n = min(len(ref), len(flat), 64)  # only first 64 coeffs for stability
        if n == 0:
            return 0.0
        num = sum(abs(int(ref[i]) - int(flat[i])) for i in range(n))
        # crude normalization to [0,1]
        den = sum(max(1, abs(int(ref[i])) + abs(int(flat[i]))) for i in range(n))
        return max(0.0, 1.0 - (num / den))

    best = 0.0
    for p in profiles:
        ref = p.get("qt", [])
        if ref:
            best = max(best, score_one(ref))
    return float(best)
