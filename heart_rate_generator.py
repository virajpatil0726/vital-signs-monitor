# Heart Rate Generator
# This simulates real heart rate data like a medical sensor would send

import numpy as np
import pandas as pd
from datetime import datetime

# Function to generate one heart rate reading
def generate_heart_rate():
    # Normal heart rate is 60-100 bpm
    heart_rate = np.random.randint(60, 101)
    return heart_rate

# Function to generate multiple readings
def generate_readings(num_readings=10):
    data = []
    for i in range(num_readings):
        reading = {
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "heart_rate": generate_heart_rate()
        }
        data.append(reading)
    return data

# Run the generator and print results
if __name__ == "__main__":
    print("=== Heart Rate Monitor ===")
    readings = generate_readings(10)
    for r in readings:
        print(f"Time: {r['timestamp']} | Heart Rate: {r['heart_rate']} bpm")