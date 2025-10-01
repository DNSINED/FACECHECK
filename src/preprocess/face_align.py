from __future__ import annotations
from typing import Dict, Tuple
import numpy as np


def align_face(img: np.ndarray) -> Tuple[np.ndarray, Dict]:
    # TODO: implement MediaPipe/RetinaFace detection and similarity transform.
    h, w = img.shape[:2]
    crop = np.zeros((384, 384, 3), dtype=np.uint8)
    meta = {"landmarks": None, "mask": None, "orig_size": (h, w)}
    return crop, meta
