from __future__ import annotations
from typing import Dict, Optional
import numpy as np


def edge_metrics(img: np.ndarray, mask: Optional[np.ndarray] = None) -> Dict[str, float]:
    # TODO: Canny/Laplacian-based metrics around hair/teeth/glasses
    return {"halo_score": 0.0, "teeth_edge_ratio": 0.0, "glasses_halo": 0.0}
