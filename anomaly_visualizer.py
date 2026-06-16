# Anomaly Visualizer
# Shows which patient readings the AI flagged as dangerous
# Makes ML results visual and easy to understand!

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import joblib
from vital_signs_simulator import generate_all_vitals
from anomaly_detector import inject_anomalies, train_model, generate_training_data

def generate_test_data():
    """Generate mixed data with some anomalies"""
    # Normal readings
    normal = generate_all_vitals(100)
    df = pd.DataFrame(normal)
    
    # Add some anomalies manually
    anomalies = []
    for i in range(15):
        anomalies.append({
            'timestamp': '00:00:00',
            'heart_rate': np.random.randint(150, 200),
            'spo2': np.random.randint(70, 88),
            'systolic': np.random.randint(160, 200),
            'diastolic': np.random.randint(100, 130)
        })
    
    anomaly_df = pd.DataFrame(anomalies)
    combined = pd.concat([df, anomaly_df], ignore_index=True)
    combined = combined.sample(frac=1).reset_index(drop=True)  # Shuffle
    return combined

def detect_anomalies_batch(model, df):
    """Run anomaly detection on entire dataset"""
    features = df[['heart_rate', 'spo2', 'systolic', 'diastolic']]
    predictions = model.predict(features)
    return predictions  # -1 = anomaly, 1 = normal

def plot_anomalies(df, predictions):
    """Plot vital signs highlighting anomalies in red"""
    
    normal_idx = predictions == 1
    anomaly_idx = predictions == -1
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('AI Anomaly Detection Results\n(Red = Flagged by AI as Dangerous)', 
                 fontsize=14, fontweight='bold')
    
    vitals = ['heart_rate', 'spo2', 'systolic', 'diastolic']
    titles = ['Heart Rate (bpm)', 'SpO2 (%)', 'Systolic BP (mmHg)', 'Diastolic BP (mmHg)']
    colors = ['blue', 'green', 'purple', 'pink']
    
    for idx, (vital, title, color) in enumerate(zip(vitals, titles, colors)):
        ax = axes[idx // 2][idx % 2]
        
        # Plot normal readings
        ax.scatter(df.index[normal_idx], df[vital][normal_idx], 
                  color=color, alpha=0.5, s=20, label='Normal')
        
        # Plot anomalies in red
        ax.scatter(df.index[anomaly_idx], df[vital][anomaly_idx],
                  color='red', alpha=0.8, s=60, label='AI Anomaly', marker='x')
        
        ax.set_title(title)
        ax.set_xlabel('Reading Number')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('anomaly_results.png', dpi=150, bbox_inches='tight')
    print("✓ Anomaly chart saved as anomaly_results.png")
    plt.show()

if __name__ == "__main__":
    print("Loading ML model...")
    model = joblib.load('anomaly_model.pkl')
    
    print("Generating test data with anomalies...")
    df = generate_test_data()
    
    print("Running AI anomaly detection...")
    predictions = detect_anomalies_batch(model, df)
    
    anomaly_count = sum(predictions == -1)
    print(f"AI detected {anomaly_count} anomalies out of {len(df)} readings!")
    
    print("Creating visualization...")
    plot_anomalies(df, predictions)