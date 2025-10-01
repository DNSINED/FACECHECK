from __future__ import annotations
import time
from dataclasses import dataclass


@dataclass
class Timer:
    start: float | None = None
    elapsed_ms: float = 0.0

    def __enter__(self) -> "Timer":
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.elapsed_ms = (time.perf_counter() - (self.start or time.perf_counter())) * 1000.0
