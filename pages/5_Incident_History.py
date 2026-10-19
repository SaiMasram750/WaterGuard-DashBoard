import pandas as pd
import streamlit as st

st.set_page_config(page_title="Incident History Log", layout="wide")

st.title("📜 Incident History & Compliance Logging")

incidents = pd.DataFrame(
    {
        "Incident ID": ["INC-2026-001", "INC-2026-002", "INC-2026-003"],
        "Timestamp": ["2026-10-19 08:12:00", "2026-10-18 14:30:15", "2026-10-17 02:45:00"],
        "Severity": ["CRITICAL", "WARNING", "SUSPICIOUS"],
        "Primary Trigger": [
            "Rule #9: Turbidity/Chlorine Inversion",
            "LSTM Sequence Loss Spike",
            "Isolation Forest Point Outlier",
        ],
        "Status": ["Unacknowledged", "Acknowledged", "Resolved"],
    }
)

st.dataframe(incidents, use_container_width=True)

selected_id = st.selectbox("Select Incident to Review:", incidents["Incident ID"])

st.text_area("Operator Investigation Notes:", "Sensor recalibrated following high turbidity alarm. Confirmed valid event.")

if st.button("📄 Generate PDF Audit Report"):
    st.success(f"Audit report for **{selected_id}** generated and saved to `outputs/reports/{selected_id}.pdf`!")
