from __future__ import annotations
import numpy as np


def compute_tabular_features(face_rgb_384: np.ndarray) -> dict[str, float]:
    # TODO: FFT peaks, energy ratios, edge metrics
    return {"fft_peaks": 0.0, "hf_ratio": 0.0, "halo_score": 0.0}
