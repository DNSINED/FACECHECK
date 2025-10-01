from __future__ import annotations
from typing import Dict, Tuple
import numpy as np


def spectrum(y_384: np.ndarray) -> Tuple[np.ndarray, Dict]:
    # TODO: log magnitude FFT and peak detection
    spec = np.zeros((384, 384), dtype=np.uint8)
    stats = {"n_peaks": 0, "hf_ratio": 0.0}
    return spec, stats
