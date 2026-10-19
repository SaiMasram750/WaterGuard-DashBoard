import streamlit as st

st.set_page_config(
    page_title="WaterGuard-X | OT Water Safety Dashboard",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("💧 WaterGuard-X")
st.caption("Cyber-Physical Safety Monitoring & Anomaly Triangulation Platform")
st.markdown("---")

col1, col2, col3, col4 = st.columns(4)
col1.metric("System Health", "99.8%", "0.2% variance")
col2.metric("Telemetry Pipeline", "Active", "Modbus TCP Sync")
col3.metric("AI Ensemble State", "🟢 Active", "Mock Hybrid Mode")
col4.metric("Active Incidents", "1 Critical", "+1 last 15m", delta_color="inverse")

st.markdown("### 🏗️ Triangulation Pipeline Architecture")
st.info(
    "WaterGuard-X mandates multi-source consensus across Isolation Forest (point outliers), "
    "LSTM Autoencoders (temporal drift), and physical conservation laws (Physics Safety Rules)."
)

st.markdown(
    """
```mermaid
graph LR
    A[OT Telemetry / Modbus TCP] --> B[Feature Normalization]
    B --> C1[Isolation Forest]
    B --> C2[LSTM Autoencoder]
    B --> C3[Physics Conservation Rules]
    C1 --> D[Hybrid Decision Engine]
    C2 --> D
    C3 --> D
    D --> E[Severity Score & Action Recommendations]
```
"""
)
