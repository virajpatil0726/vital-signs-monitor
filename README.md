# 🏥 Patient Vital Signs Monitor Simulator

A Python-based medical device simulator that generates, monitors, 
and logs real-time patient vital signs data.

Built as part of my Medical Systems Engineering portfolio.

## 📊 Features
- Real-time Heart Rate simulation (60-100 bpm)
- SpO2 (Oxygen Level) monitoring (95-100%)
- Blood Pressure tracking (systolic/diastolic)
- Automatic CSV data logging like real medical devices

## 🛠️ Technologies Used
- Python 3.11
- NumPy - data generation
- Pandas - data management and CSV export

## 🚀 How to Run

**Install dependencies:**
```
pip install numpy pandas streamlit
```

**Run the simulator:**
```
py -3.11 vital_signs_simulator.py
```

**Save data to CSV:**
```
py -3.11 save_data.py
```

## 📁 Project Structure
- `heart_rate_generator.py` - Heart rate simulation
- `vital_signs_simulator.py` - Full vital signs simulator
- `save_data.py` - Data logging to CSV

## 👨‍💻 Author
Viraj Patil - Medical Systems Engineering Student