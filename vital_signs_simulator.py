# Vital Signs Simulator
# Simulates heart rate, SpO2, and blood pressure like a real medical device

import numpy as np
import pandas as pd
from datetime import datetime

# --- HEART RATE GENERATOR ---
def generate_heart_rate():
    # Normal: 60-100 bpm
    return np.random.randint(60, 101)

# --- SpO2 GENERATOR ---
def generate_spo2():
    # Normal: 95-100%
    return np.random.randint(95, 101)

# --- BLOOD PRESSURE GENERATOR ---
def generate_blood_pressure():
    # Normal systolic: 90-120, diastolic: 60-80
    systolic = np.random.randint(90, 121)
    diastolic = np.random.randint(60, 81)
    return systolic, diastolic

# --- GENERATE ALL VITALS TOGETHER ---
def generate_all_vitals(num_readings=10):
    data = []
    for i in range(num_readings):
        systolic, diastolic = generate_blood_pressure()
        reading = {
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "heart_rate": generate_heart_rate(),
            "spo2": generate_spo2(),
            "systolic": systolic,
            "diastolic": diastolic
        }
        data.append(reading)
    return data

# --- RUN AND DISPLAY ---
if __name__ == "__main__":
    print("=== Patient Vital Signs Monitor ===")
    print(f"{'Time':<12} {'Heart Rate':<15} {'SpO2':<10} {'Blood Pressure'}")
    print("-" * 50)
    
    readings = generate_all_vitals(10)
    for r in readings:
        print(f"{r['timestamp']:<12} {r['heart_rate']} bpm{'':<8} {r['spo2']}%{'':<6} {r['systolic']}/{r['diastolic']} mmHg")