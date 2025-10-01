from __future__ import annotations
from typing import Dict
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def render_report(ctx: Dict, out_path: str) -> str:
    c = canvas.Canvas(out_path, pagesize=A4)
    c.setTitle("FakeCheck Report (stub)")
    c.drawString(72, 800, "FakeCheck Report (stub)")
    c.drawString(72, 780, f"Verdict: {ctx.get('verdict','Inconclusive')}")
    c.drawString(72, 760, f"Score: {ctx.get('score',0.5):.2f}")
    c.showPage()
    c.save()
    return out_path
