import streamlit as st
import sys
import os

# Add src folder to path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_PATH = os.path.join(BASE_DIR, "src")
sys.path.append(SRC_PATH)

from data_loader import load_data
from decision_engine import generate_decisions


# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="AI Decision Engine",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("📊 AI Retail Decision Engine")
st.write("Upload your dataset and get intelligent business decisions instantly.")

# -----------------------------
# File Upload
# -----------------------------
uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])


# -----------------------------
# Load Data
# -----------------------------
if uploaded_file is not None:
    df = load_data(uploaded_file)
    st.success("✅ Data loaded successfully!")

else:
    st.info("Using default dataset")
    DATA_PATH = os.path.join(BASE_DIR, "data", "superstore.csv")
    df = load_data(DATA_PATH)


# -----------------------------
# Generate Decisions
# -----------------------------
if st.button("🚀 Generate Decisions"):

    decisions = generate_decisions(df)

    st.subheader("📌 Top Business Decisions")

    # Metrics
    st.metric("Total Decisions", len(decisions))

    st.write("---")

    # Display decisions
    for d in decisions:

        if d['priority'] == "HIGH":
            st.error(f"#{d['rank']} [HIGH] {d['decision']}")
        elif d['priority'] == "MEDIUM":
            st.warning(f"#{d['rank']} [MEDIUM] {d['decision']}")
        else:
            st.info(f"#{d['rank']} [LOW] {d['decision']}")

        st.write(f"**Reason:** {d['reason']}")
        st.write(f"**Confidence:** {d['confidence']}")
        st.write(f"**Score:** {round(d['score'], 2)}")

        st.write("---")