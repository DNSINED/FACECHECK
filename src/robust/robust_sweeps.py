from __future__ import annotations
import numpy as np


def apply_perturbations(img: np.ndarray) -> list[np.ndarray]:
    # TODO: JPEG q=80, blur sigma~0.5, resize 0.8x
    return [img.copy(), img.copy(), img.copy()]


def stability_flag(base_score: float, scores: list[float], delta: float = 0.10) -> bool:
    flips = any(((s >= 0.5) != (base_score >= 0.5)) for s in scores)
    drift = max(abs(s - base_score) for s in scores) if scores else 0.0
    return flips or (drift > delta)
