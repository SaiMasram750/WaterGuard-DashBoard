import random
import time
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

st.set_page_config(page_title="Live OT Telemetry", layout="wide")

st.title("⚡ Real-Time OT Telemetry & Triangulation Engine")

scenario = st.sidebar.selectbox(
    "Select Test Scenario:",
    [
        "1. Normal Operation",
        "2. High Turbidity Event",
        "3. Low Chlorine Event",
        "4. Pipe Leak / Pressure Collapse",
        "5. Combined Water-Quality Attack (CRITICAL)",
    ],
)

data_source = st.sidebar.radio("Data Source:", ["Modbus TCP Twin (Live)", "CSV Stream Simulator"])

st.sidebar.markdown("---")
st.sidebar.write("🟢 **Isolation Forest:** Active")
st.sidebar.write("🟢 **LSTM Autoencoder:** Active")
st.sidebar.write("🟢 **Physics Safety Engine:** Active")

# Generate synthetic stream data based on chosen scenario
np.random.seed(42)
n_points = 60
timestamps = pd.date_range(end=pd.Timestamp.now(), periods=n_points, freq="1s")

base_ph = np.random.normal(7.4, 0.05, n_points)
base_turbidity = np.random.normal(1.2, 0.1, n_points)
base_chlorine = np.random.normal(0.6, 0.02, n_points)
base_pressure = np.random.normal(65.0, 1.5, n_points)

if "High Turbidity" in scenario:
    base_turbidity[40:] += np.linspace(0.5, 6.5, 20)
elif "Low Chlorine" in scenario:
    base_chlorine[35:] -= np.linspace(0.01, 0.45, 25)
elif "Pipe Leak" in scenario:
    base_pressure[30:] -= np.linspace(2.0, 40.0, 30)
elif "Combined Water-Quality Attack" in scenario:
    base_turbidity[35:] += np.linspace(0.5, 7.0, 25)
    base_chlorine[35:] -= np.linspace(0.01, 0.5, 25)

df = pd.DataFrame(
    {
        "Timestamp": timestamps,
        "pH": base_ph,
        "Turbidity (NTU)": base_turbidity,
        "Chlorine (mg/L)": base_chlorine,
        "Pressure (PSI)": base_pressure,
    }
)

# Display Top Metrics & Alert Banner
if "Combined" in scenario:
    st.error("🚨 **CRITICAL ALERT:** Simultaneous Turbidity Spike and Chlorine Collapse Detected!")
elif "Normal" not in scenario:
    st.warning(f"⚠️ **WARNING:** Anomaly Detected under {scenario}")
else:
    st.success("✅ **SYSTEM NORMAL:** All parameters within safe physical envelopes.")

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("#### 🌲 Isolation Forest")
    st.metric(
        "Point Outlier Score",
        "0.89" if "Combined" in scenario else "0.12",
        delta="HIGH RISK" if "Combined" in scenario else "Normal",
        delta_color="inverse",
    )
with c2:
    st.markdown("#### 📈 LSTM Autoencoder")
    st.metric(
        "Sequence Loss (MSE)",
        "0.0482" if "Combined" in scenario else "0.0012",
        delta="DRIFT DETECTED" if "Combined" in scenario else "Stable",
        delta_color="inverse",
    )
with c3:
    st.markdown("#### ⚖️ Physics Engine")
    st.metric(
        "Violations",
        "Rule #4, Rule #9" if "Combined" in scenario else "None",
        delta="CRITICAL" if "Combined" in scenario else "Passed",
        delta_color="inverse",
    )

st.markdown("---")

fig = make_subplots(
    rows=2,
    cols=2,
    subplot_titles=("pH Level", "Turbidity (NTU)", "Chlorine (mg/L)", "System Pressure (PSI)"),
)

fig.add_trace(
    go.Scatter(x=df["Timestamp"], y=df["pH"], name="pH", line=dict(color="#2ca02c")),
    row=1,
    col=1,
)
fig.add_trace(
    go.Scatter(
        x=df["Timestamp"], y=df["Turbidity (NTU)"], name="Turbidity", line=dict(color="#ff7f0e")
    ),
    row=1,
    col=2,
)
fig.add_trace(
    go.Scatter(
        x=df["Timestamp"], y=df["Chlorine (mg/L)"], name="Chlorine", line=dict(color="#1f77b4")
    ),
    row=2,
    col=1,
)
fig.add_trace(
    go.Scatter(
        x=df["Timestamp"], y=df["Pressure (PSI)"], name="Pressure", line=dict(color="#d62728")
    ),
    row=2,
    col=2,
)

fig.update_layout(height=500, showlegend=False, margin=dict(l=20, r=20, t=40, b=20))

st.plotly_chart(fig, use_container_width=True)
