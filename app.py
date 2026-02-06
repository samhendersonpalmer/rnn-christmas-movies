import streamlit as st
import subprocess
import sys
from pathlib import Path


# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="Christmas Movie Generator",
    page_icon="🎄",
    layout="centered"
)

st.snow()

st.markdown("""
<style>
[data-testid="stSnow"] {
    opacity: 0.5;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# Christmas Theme Styling
# -------------------------
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(to bottom, #0f5132, #14532d);
        }
        .christmas-title {
            font-size: 48px;
            font-weight: bold;
            color: #ff4b4b;
            text-align: center;
            text-shadow: 2px 2px #0f5132;
        }
        .festive-output {
            background-color: #062e1f;
            color: #f8f9fa;
            padding: 1.5rem;
            border-radius: 15px;
            font-family: "Courier New", monospace;
            font-size: 18px;
            border: 2px dashed #ff4b4b;
            white-space: pre-wrap;
        }
        div.stButton > button {
            background-color: #ff4b4b;
            color: white;
            font-size: 22px;
            padding: 0.75em 2em;
            border-radius: 15px;
            border: none;
        }
        div.stButton > button:hover {
            background-color: #e63946;
            transform: scale(1.05);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------
# Title
# -------------------------
st.markdown('<div class="christmas-title"> Christmas Movie Generator </div>', unsafe_allow_html=True)
st.write("")
st.write("")

# -------------------------
# Centered Button
# -------------------------
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    run_button = st.button("Generate")

# -------------------------
# Script Execution
# -------------------------
if run_button:
    script_path = Path("src/main.py")

    if not script_path.exists():
        st.error("❌ src/main.py not found!")
    else:
        try:
            result = subprocess.run(
                [sys.executable, str(script_path)],
                capture_output=True,
                text=True
            )

            output_text = result.stdout.strip()
            error_text = result.stderr.strip()

            st.markdown("### 🎁 Generated Output")

            if output_text:
                st.markdown(
                    f'<div class="festive-output">{output_text}</div>',
                    unsafe_allow_html=True
                )

            if error_text:
                st.error(error_text)

        except Exception as e:
            st.error(f"Execution failed: {e}")
