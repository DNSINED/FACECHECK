from __future__ import annotations
import numpy as np
from PIL import Image


def read_image(path: str) -> np.ndarray:
    # TODO: implement robust reading (keep EXIF bytes elsewhere)
    return np.zeros((384, 384, 3), dtype=np.uint8)


def to_pil(img: np.ndarray) -> Image.Image:
    return Image.fromarray(img)
