from __future__ import annotations
import torch
import torch.nn as nn


class FFTHead(nn.Module):
    def __init__(self, in_ch: int = 1, d_fft: int = 256) -> None:
        super().__init__()
        # Tiny conv stack placeholder
        self.net = nn.Sequential(
            nn.Conv2d(in_ch, 32, 3, padding=1),
            nn.ReLU(inplace=True),
            nn.AdaptiveAvgPool2d(1),
        )
        self.proj = nn.Linear(32, d_fft)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.net(x).flatten(1)
        return self.proj(x)
