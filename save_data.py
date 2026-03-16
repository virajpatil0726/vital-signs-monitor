# Save Vital Signs Data to CSV
# Just like real medical devices log patient data to files

import pandas as pd
from vital_signs_simulator import generate_all_vitals
from datetime import datetime

def save_to_csv(num_readings=50):
    # Generate 50 vital sign readings
    print("Generating vital signs data...")
    readings = generate_all_vitals(num_readings)
    
    # Convert to a pandas table (like Excel)
    df = pd.DataFrame(readings)
    
    # Create a filename with today's date
    filename = f"patient_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    
    # Save to CSV file
    df.to_csv(filename, index=False)
    
    print(f"✓ Saved {num_readings} readings to {filename}")
    print("\nFirst 5 readings:")
    print(df.head())
    
    return df

if __name__ == "__main__":
    save_to_csv()