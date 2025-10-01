import numpy as np
from src.preprocess.face_align import align_face


def test_align_face_shape():
    img = np.zeros((720, 1280, 3), dtype=np.uint8)
    crop, meta = align_face(img)
    assert crop.shape == (384, 384, 3)
    assert "orig_size" in meta
