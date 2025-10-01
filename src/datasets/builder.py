from __future__ import annotations
from typing import Dict, List
from pathlib import Path
import csv
import numpy as np


class FakeCheckDataset:
    def __init__(self, manifest_csv: str) -> None:
        """
        Args:
            manifest_csv: CSV with columns [path,label]
        """
        self.items: List[Dict] = []
        with open(manifest_csv, "r", newline="") as f:
            for row in csv.DictReader(f):
                self.items.append({"path": row["path"], "label": int(row["label"])})

    def __len__(self) -> int:
        return len(self.items)

    def __getitem__(self, idx: int) -> Dict:
        # TODO: load image and apply augmentations
        item = self.items[idx]
        img = np.zeros((384, 384, 3), dtype=np.uint8)
        return {"image": img, "label": item["label"], "path": item["path"]}
