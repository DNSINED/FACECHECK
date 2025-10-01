from __future__ import annotations
import torch
import torch.nn as nn


class FusionHead(nn.Module):
    def __init__(self, d_rgb: int, d_fft: int, d_tab: int = 0) -> None:
        super().__init__()
        d_in = d_rgb + d_fft + (d_tab or 0)
        self.mlp = nn.Sequential(
            nn.Linear(d_in, 128), nn.ReLU(inplace=True), nn.Dropout(0.1), nn.Linear(128, 1)
        )

    def forward(self, f_rgb: torch.Tensor, f_fft: torch.Tensor, f_tab: torch.Tensor | None = None) -> torch.Tensor:
        parts = [f_rgb, f_fft] + ([f_tab] if f_tab is not None else [])
        x = torch.cat(parts, dim=1)
        return self.mlp(x)
