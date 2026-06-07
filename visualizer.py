# Vital Signs Visualizer
# Creates charts and graphs of patient data
# Like real medical reports!

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from vital_signs_simulator import generate_all_vitals

def generate_chart_data(num_readings=50):
    """Generate data for charts"""
    readings = generate_all_vitals(num_readings)
    df = pd.DataFrame(readings)
    return df

def plot_vital_signs(df):
    """Create a professional 3-panel chart"""
    
    fig, axes = plt.subplots(3, 1, figsize=(12, 10))
    fig.suptitle('Patient Vital Signs Report', fontsize=16, fontweight='bold')
    
    # Chart 1 - Heart Rate
    axes[0].plot(df['heart_rate'], color='red', linewidth=2, label='Heart Rate')
    axes[0].axhline(y=100, color='orange', linestyle='--', label='Max Normal (100)')
    axes[0].axhline(y=60, color='orange', linestyle='--', label='Min Normal (60)')
    axes[0].fill_between(range(len(df)), 60, 100, alpha=0.1, color='green')
    axes[0].set_ylabel('Heart Rate (bpm)')
    axes[0].set_title('Heart Rate Over Time')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    # Chart 2 - SpO2
    axes[1].plot(df['spo2'], color='blue', linewidth=2, label='SpO2')
    axes[1].axhline(y=95, color='orange', linestyle='--', label='Min Normal (95%)')
    axes[1].fill_between(range(len(df)), 95, 100, alpha=0.1, color='green')
    axes[1].set_ylabel('SpO2 (%)')
    axes[1].set_title('Oxygen Saturation Over Time')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    # Chart 3 - Blood Pressure
    axes[2].plot(df['systolic'], color='purple', linewidth=2, label='Systolic')
    axes[2].plot(df['diastolic'], color='pink', linewidth=2, label='Diastolic')
    axes[2].axhline(y=120, color='orange', linestyle='--', label='Max Normal Systolic')
    axes[2].fill_between(range(len(df)), 0, 120, alpha=0.1, color='green')
    axes[2].set_ylabel('Blood Pressure (mmHg)')
    axes[2].set_title('Blood Pressure Over Time')
    axes[2].legend()
    axes[2].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('vital_signs_report.png', dpi=150, bbox_inches='tight')
    print("✓ Chart saved as vital_signs_report.png")
    plt.show()

if __name__ == "__main__":
    print("Generating patient data...")
    df = generate_chart_data(50)
    print("Creating charts...")
    plot_vital_signs(df)
    print("Done!")