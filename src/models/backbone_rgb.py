from __future__ import annotations
import torch
import torch.nn as nn


class RGBBackbone(nn.Module):
    def __init__(self, name: str = "tf_efficientnet_b4_ns", feat_dim: int = 1792) -> None:
        super().__init__()
        # TODO: load timm backbone and pool to feat_dim
        self.feat_dim = feat_dim
        self.pool = nn.AdaptiveAvgPool2d(1)
        self.stub = nn.Conv2d(3, feat_dim, kernel_size=1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.pool(self.stub(x))  # (B, D, 1, 1)
        return x.flatten(1)
