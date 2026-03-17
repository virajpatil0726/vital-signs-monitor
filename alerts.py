# Alert System for Patient Vital Signs Monitor
# Detects dangerous readings and triggers warnings
# Just like a real ICU alarm system!

# ============================================
# ALERT THRESHOLDS (medical standards)
# ============================================

HEART_RATE_LOW = 60
HEART_RATE_HIGH = 100
SPO2_LOW = 95
SYSTOLIC_HIGH = 120
DIASTOLIC_HIGH = 80

# ============================================
# ALERT FUNCTIONS
# ============================================

def check_heart_rate(heart_rate):
    """Check if heart rate is in safe range"""
    if heart_rate > HEART_RATE_HIGH:
        return "CRITICAL", f"Heart rate TOO HIGH: {heart_rate} bpm (max {HEART_RATE_HIGH})"
    elif heart_rate < HEART_RATE_LOW:
        return "CRITICAL", f"Heart rate TOO LOW: {heart_rate} bpm (min {HEART_RATE_LOW})"
    else:
        return "OK", f"Heart rate normal: {heart_rate} bpm"

def check_spo2(spo2):
    """Check if oxygen level is safe"""
    if spo2 < SPO2_LOW:
        return "CRITICAL", f"SpO2 TOO LOW: {spo2}% (min {SPO2_LOW}%)"
    else:
        return "OK", f"SpO2 normal: {spo2}%"

def check_blood_pressure(systolic, diastolic):
    """Check if blood pressure is safe"""
    if systolic > SYSTOLIC_HIGH:
        return "WARNING", f"Systolic HIGH: {systolic} mmHg (max {SYSTOLIC_HIGH})"
    elif diastolic > DIASTOLIC_HIGH:
        return "WARNING", f"Diastolic HIGH: {diastolic} mmHg (max {DIASTOLIC_HIGH})"
    else:
        return "OK", f"Blood pressure normal: {systolic}/{diastolic} mmHg"

def check_all_vitals(reading):
    """Check all vital signs and return list of alerts"""
    alerts = []
    
    hr_status, hr_msg = check_heart_rate(reading['heart_rate'])
    spo2_status, spo2_msg = check_spo2(reading['spo2'])
    bp_status, bp_msg = check_blood_pressure(reading['systolic'], reading['diastolic'])
    
    alerts.append({"type": hr_status, "message": hr_msg})
    alerts.append({"type": spo2_status, "message": spo2_msg})
    alerts.append({"type": bp_status, "message": bp_msg})
    
    return alerts

# ============================================
# TEST THE ALERT SYSTEM
# ============================================

if __name__ == "__main__":
    # Test with normal reading
    normal_reading = {
        "heart_rate": 75,
        "spo2": 98,
        "systolic": 110,
        "diastolic": 70
    }
    
    # Test with dangerous reading
    dangerous_reading = {
        "heart_rate": 130,
        "spo2": 88,
        "systolic": 150,
        "diastolic": 95
    }
    
    print("=== NORMAL PATIENT ===")
    for alert in check_all_vitals(normal_reading):
        print(f"[{alert['type']}] {alert['message']}")
    
    print("\n=== CRITICAL PATIENT ===")
    for alert in check_all_vitals(dangerous_reading):
        print(f"[{alert['type']}] {alert['message']}")