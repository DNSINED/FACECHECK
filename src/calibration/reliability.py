from __future__ import annotations
import numpy as np


def expected_calibration_error(probs: np.ndarray, labels: np.ndarray, n_bins: int = 15) -> float:
    # TODO: implement ECE
    return 0.0


def confidence_band(prob: float, bin_var: float = 0.0025) -> tuple[float, float]:
    lo = max(0.0, prob - bin_var ** 0.5)
    hi = min(1.0, prob + bin_var ** 0.5)
    return lo, hi
