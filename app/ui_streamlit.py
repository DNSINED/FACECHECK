from __future__ import annotations
import io
import base64
from datetime import datetime
from typing import Tuple

import numpy as np
from PIL import Image
import streamlit as st

st.set_page_config(page_title="FakeCheck", layout="wide")


def _mock_infer(img: Image.Image) -> Tuple[str, float, Tuple[float, float], bool]:
    rng = np.random.default_rng(0)
    score = float(rng.uniform(0.45, 0.55))
    band = (max(0.0, score - 0.05), min(1.0, score + 0.05))
    return "Inconclusive", score, band, False


def _img_to_b64(img: Image.Image) -> str:
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode("utf-8")


st.title("🔍 FakeCheck — Deepfake Headshot Detector (Preview)")
st.caption("This is a placeholder UI. Model & forensics pipelines are stubs.")

with st.sidebar:
    st.header("Settings")
    st.toggle("Dark mode", value=True, help="UI preference only")
    st.write("Thresholds (read from configs/thresholds.yml in real app)")

tab1, tab2 = st.tabs(["Single Image", "Batch"])

with tab1:
    up = st.file_uploader("Upload a portrait image", type=["jpg", "jpeg", "png"])
    if up:
        img = Image.open(up).convert("RGB")
        verdict, score, band, unstable = _mock_infer(img)

        c1, c2 = st.columns([1, 1])
        with c1:
            st.image(img, caption="Input image", use_column_width=True)
        with c2:
            st.metric("Verdict", verdict)
            st.metric("Score", f"{score:.2f}")
            st.write(f"Confidence band: [{band[0]:.2f}, {band[1]:.2f}]")
            st.write(f"Stability: {'Unstable' if unstable else 'Stable'}")
            st.download_button(
                "Download JSON (mock)",
                data=(
                    f'{{"verdict":"{verdict}","score":{score:.3f},"band":[{band[0]:.3f},{band[1]:.3f}],"unstable":{str(unstable).lower()},"ts":"{datetime.utcnow().isoformat()}Z"}}'
                ),
                file_name="fakecheck_result.json",
                mime="application/json",
            )
        with st.expander("Details: Heatmap / FFT / Provenance (placeholders)"):
            st.image(img, caption="(Placeholder) Heatmap overlay")
            st.image(img, caption="(Placeholder) FFT spectrum")
            st.json({"exif_present": None, "qt_match_score": None})

with tab2:
    st.info("Batch mode placeholder: drop a folder in the CLI for now.")
