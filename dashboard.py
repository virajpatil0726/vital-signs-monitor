# Patient Vital Signs Dashboard
# Displays live vital signs in a browser using Streamlit

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

# Create 3 columns for the 3 vital signs
col1, col2, col3 = st.columns(3)

# Placeholders for live updating
heart_rate_box = col1.empty()
spo2_box = col2.empty()
bp_box = col3.empty()

st.divider()
st.subheader("📊 Live Readings")
table_placeholder = st.empty()

# Live update loop
readings_history = []

for i in range(100):  # Run 100 times
    # Generate new reading
    reading = generate_all_vitals(1)[0]
    readings_history.append(reading)
    
    # Keep only last 10 readings
    if len(readings_history) > 10:
        readings_history = readings_history[-10:]
    
    # Update the boxes with current values
    heart_rate_box.metric(
        label="❤️ Heart Rate",
        value=f"{reading['heart_rate']} bpm"
    )
    
    spo2_box.metric(
        label="🫁 SpO2",
        value=f"{reading['spo2']} %"
    )
    
    bp_box.metric(
        label="🩸 Blood Pressure",
        value=f"{reading['systolic']}/{reading['diastolic']} mmHg"
    )
    
    # Update table with history
    table_placeholder.table(readings_history)
    
    # Wait 1 second before next reading
    time.sleep(1)