import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Model Triangulation Matrix", layout="wide")

st.title("🔬 Triangulation & Model Comparison Matrix")

st.markdown("Compare detection flags across the three detection engines for sample events:")

mock_comparison = pd.DataFrame(
    {
        "Event Description": [
            "Transient Sensor Spike",
            "Gradual Chemical Disinfectant Decay",
            "Physical Pipe Burst",
            "Spoofed Telemetry Attack",
            "Normal Operations",
        ],
        "Isolation Forest": ["FLAGGED 🔴", "OK 🟢", "FLAGGED 🔴", "OK 🟢", "OK 🟢"],
        "LSTM Autoencoder": ["OK 🟢", "FLAGGED 🔴", "FLAGGED 🔴", "FLAGGED 🔴", "OK 🟢"],
        "Physics Safety Rules": ["OK 🟢", "FLAGGED 🔴", "FLAGGED 🔴", "FLAGGED 🔴", "OK 🟢"],
        "Fused Final Consensus": [
            "SUSPICIOUS 🟡",
            "WARNING 🟠",
            "CRITICAL 🔴",
            "CRITICAL 🔴",
            "NORMAL 🟢",
        ],
    }
)

st.dataframe(mock_comparison, use_container_width=True)
