# Patient Vital Signs Dashboard with AI Anomaly Detection
# Combines live monitoring + rule-based alerts + ML anomaly detection

import streamlit as st
import time
import joblib
import pandas as pd
from vital_signs_simulator import generate_all_vitals
from alerts import check_all_vitals
from anomaly_detector import detect_anomaly, train_model, generate_training_data, inject_anomalies
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="AI Patient Monitor",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("🤖 AI-Powered Patient Vital Signs Monitor")
st.markdown("**Real-time monitoring with Machine Learning anomaly detection**")
st.divider()

# Load or train model
@st.cache_resource
def load_model():
    try:
        model = joblib.load('anomaly_model.pkl')
        return model
    except:
        st.warning("Training new model...")
        data = generate_training_data(1000)
        data = inject_anomalies(data, 50)
        model = train_model(data)
        return model

model = load_model()

# Create columns
col1, col2, col3 = st.columns(3)
heart_rate_box = col1.empty()
spo2_box = col2.empty()
bp_box = col3.empty()

st.divider()

# Alert boxes
rule_alert_box = st.empty()
ml_alert_box = st.empty()

st.subheader("📊 Live Readings")
table_placeholder = st.empty()

readings_history = []

for i in range(100):
    reading = generate_all_vitals(1)[0]
    readings_history.append(reading)

    if len(readings_history) > 10:
        readings_history = readings_history[-10:]

    hr = reading['heart_rate']
    spo2 = reading['spo2']
    systolic = reading['systolic']
    diastolic = reading['diastolic']

    # Rule based alerts
    alerts = check_all_vitals(reading)
    critical = [a for a in alerts if a['type'] == 'CRITICAL']

    if critical:
        rule_alert_box.error("🚨 RULE ALERT: " + " | ".join([a['message'] for a in critical]))
    else:
        rule_alert_box.success("✅ Rule Check: All vital signs NORMAL")

    # ML anomaly detection
    is_anomaly = detect_anomaly(model, reading)
    if is_anomaly:
        ml_alert_box.error("🤖 AI ALERT: Anomaly detected in patient readings!")
    else:
        ml_alert_box.success("🤖 AI Check: Readings appear NORMAL")

    # Update metrics
    heart_rate_box.metric(
        label="❤️ Heart Rate",
        value=f"{hr} bpm",
        delta="Normal" if 60 <= hr <= 100 else "WARNING"
    )

    spo2_box.metric(
        label="🫁 SpO2",
        value=f"{spo2} %",
        delta="Normal" if spo2 >= 95 else "WARNING"
    )

    bp_box.metric(
        label="🩸 Blood Pressure",
        value=f"{systolic}/{diastolic} mmHg",
        delta="Normal" if systolic <= 120 else "WARNING"
    )

    table_placeholder.table(readings_history)
    time.sleep(1)