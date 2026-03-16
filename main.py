# ============================================
# Patient Vital Signs Monitor Simulator
# Author: Viraj Patil
# Field: Medical Systems Engineering
# Description: Simulates real medical device
#              data like Dräger patient monitors
# ============================================

from vital_signs_simulator import generate_all_vitals
from save_data import save_to_csv
import pandas as pd

def display_vitals(readings):
    """Display vital signs in a clean table format"""
    print("\n" + "="*55)
    print("       PATIENT VITAL SIGNS MONITOR")
    print("="*55)
    print(f"{'Time':<12} {'Heart Rate':<15} {'SpO2':<10} {'Blood Pressure'}")
    print("-"*55)
    
    for r in readings:
        # Check for abnormal values
        hr_status = "⚠️ HIGH" if r['heart_rate'] > 100 else "✓ OK"
        spo2_status = "⚠️ LOW" if r['spo2'] < 95 else "✓ OK"
        
        print(f"{r['timestamp']:<12} {r['heart_rate']} bpm [{hr_status}]")
        print(f"{'':>12} SpO2: {r['spo2']}% [{spo2_status}]")
        print(f"{'':>12} BP: {r['systolic']}/{r['diastolic']} mmHg")
        print("-"*55)

def run_monitor():
    """Main function to run the vital signs monitor"""
    print("\nStarting Patient Vital Signs Monitor...")
    print("Simulating medical sensor data...\n")
    
    # Generate readings
    readings = generate_all_vitals(5)
    
    # Display on screen
    display_vitals(readings)
    
    # Save to CSV
    print("\nSaving data to CSV file...")
    save_to_csv(50)
    
    print("\nMonitor session complete!")

if __name__ == "__main__":
    run_monitor()