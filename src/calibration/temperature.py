from __future__ import annotations
import numpy as np


def fit_temperature(logits: np.ndarray, labels: np.ndarray) -> float:
    # TODO: optimize NLL to find T
    return 1.0


def apply_temperature(logits: np.ndarray, T: float) -> np.ndarray:
    return logits / max(T, 1e-6)
