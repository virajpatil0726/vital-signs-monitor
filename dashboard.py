# Patient Vital Signs Dashboard with Color Alerts
# Green = Normal, Red = Dangerous

import streamlit as st
import time
from vital_signs_simulator import generate_all_vitals

# Page configuration
st.set_page_config(
    page_title="Patient Vital Signs Monitor",
    page_icon="🏥",
    layout="wide"
)

# Title
st.title("🏥 Patient Vital Signs Monitor")
st.markdown("**Real-time patient monitoring simulation**")
st.divider()

# Create 3 columns
col1, col2, col3 = st.columns(3)

# Placeholders
heart_rate_box = col1.empty()
spo2_box = col2.empty()
bp_box = col3.empty()

st.divider()
alert_box = st.empty()
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
    
    # Check for dangerous values
    alerts = []
    if hr > 100:
        alerts.append(f"🔴 HIGH Heart Rate: {hr} bpm")
    if hr < 60:
        alerts.append(f"🔴 LOW Heart Rate: {hr} bpm")
    if spo2 < 95:
        alerts.append(f"🔴 LOW SpO2: {spo2}%")
    if systolic > 120:
        alerts.append(f"🔴 HIGH Blood Pressure: {systolic}/{diastolic} mmHg")
    
    # Show alerts or green status
    if alerts:
        alert_box.error("⚠️ ALERT: " + " | ".join(alerts))
    else:
        alert_box.success("✅ All vital signs are NORMAL")
    
    # Delta shows change direction
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