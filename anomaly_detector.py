# Anomaly Detector for Patient Vital Signs
# Uses Machine Learning to detect abnormal readings
# Algorithm: Isolation Forest (used in real medical AI systems)

import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
from vital_signs_simulator import generate_all_vitals

# ============================================
# STEP 1: GENERATE TRAINING DATA
# ============================================

def generate_training_data(num_readings=1000):
    """Generate 1000 normal readings to train the model"""
    print("Generating training data...")
    readings = generate_all_vitals(num_readings)
    df = pd.DataFrame(readings)
    
    # We only need the numbers, not the timestamp
    features = df[['heart_rate', 'spo2', 'systolic', 'diastolic']]
    return features

# ============================================
# STEP 2: INJECT SOME ANOMALIES
# ============================================

def inject_anomalies(df, num_anomalies=50):
    """Add some fake dangerous readings to the dataset"""
    print(f"Injecting {num_anomalies} anomalies...")
    
    anomalies = []
    for i in range(num_anomalies):
        anomaly = {
            'heart_rate': np.random.choice([
                np.random.randint(150, 200),  # Very high HR
                np.random.randint(20, 40)      # Very low HR
            ]),
            'spo2': np.random.randint(70, 88),      # Dangerously low SpO2
            'systolic': np.random.randint(160, 200), # Very high BP
            'diastolic': np.random.randint(100, 130) # Very high diastolic
        }
        anomalies.append(anomaly)
    
    anomaly_df = pd.DataFrame(anomalies)
    combined = pd.concat([df, anomaly_df], ignore_index=True)
    return combined

# ============================================
# STEP 3: TRAIN THE MODEL
# ============================================

def train_model(data):
    """Train Isolation Forest model"""
    print("Training ML model...")
    
    model = IsolationForest(
        contamination=0.05,  # We expect ~5% anomalies
        random_state=42
    )
    
    model.fit(data)
    print("Model trained successfully!")
    return model

# ============================================
# STEP 4: SAVE THE MODEL
# ============================================

def save_model(model, filename='anomaly_model.pkl'):
    """Save trained model to file"""
    joblib.dump(model, filename)
    print(f"Model saved to {filename}")

# ============================================
# STEP 5: DETECT ANOMALIES
# ============================================

def detect_anomaly(model, reading):
    """Check if a single reading is anomalous"""
    data = [[
        reading['heart_rate'],
        reading['spo2'],
        reading['systolic'],
        reading['diastolic']
    ]]
    
    prediction = model.predict(data)
    # Isolation Forest returns -1 for anomaly, 1 for normal
    return prediction[0] == -1

# ============================================
# MAIN - RUN EVERYTHING
# ============================================

if __name__ == "__main__":
    # Generate and prepare data
    normal_data = generate_training_data(1000)
    full_data = inject_anomalies(normal_data, 50)
    
    # Train and save model
    model = train_model(full_data)
    save_model(model)
    
    # Test with normal reading
    normal_reading = {
        'heart_rate': 75, 'spo2': 98,
        'systolic': 110, 'diastolic': 70
    }
    
    # Test with dangerous reading
    dangerous_reading = {
        'heart_rate': 180, 'spo2': 75,
        'systolic': 190, 'diastolic': 120
    }
    
    print("\n=== ANOMALY DETECTION TEST ===")
    print(f"Normal reading anomaly: {detect_anomaly(model, normal_reading)}")
    print(f"Dangerous reading anomaly: {detect_anomaly(model, dangerous_reading)}")