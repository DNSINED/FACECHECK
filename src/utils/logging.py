from __future__ import annotations
import json
from typing import Any


def audit_log_line(**kwargs: Any) -> str:
    return json.dumps(kwargs, separators=(",", ":"))
