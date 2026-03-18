# Automated Tests for the Alert System
# Testing that our ICU alarms trigger correctly!

from alerts import check_heart_rate, check_spo2, check_blood_pressure, check_all_vitals

# ============================================
# HEART RATE ALERT TESTS
# ============================================

def test_normal_heart_rate_returns_ok():
    """Normal heart rate should return OK"""
    status, message = check_heart_rate(75)
    assert status == "OK"

def test_high_heart_rate_returns_critical():
    """Heart rate above 100 should return CRITICAL"""
    status, message = check_heart_rate(130)
    assert status == "CRITICAL"

def test_low_heart_rate_returns_critical():
    """Heart rate below 60 should return CRITICAL"""
    status, message = check_heart_rate(40)
    assert status == "CRITICAL"

def test_heart_rate_exactly_100_is_ok():
    """Heart rate of exactly 100 should be OK"""
    status, message = check_heart_rate(100)
    assert status == "OK"

def test_heart_rate_exactly_60_is_ok():
    """Heart rate of exactly 60 should be OK"""
    status, message = check_heart_rate(60)
    assert status == "OK"

# ============================================
# SpO2 ALERT TESTS
# ============================================

def test_normal_spo2_returns_ok():
    """Normal SpO2 should return OK"""
    status, message = check_spo2(98)
    assert status == "OK"

def test_low_spo2_returns_critical():
    """SpO2 below 95 should return CRITICAL"""
    status, message = check_spo2(88)
    assert status == "CRITICAL"

def test_spo2_exactly_95_is_ok():
    """SpO2 of exactly 95 should be OK"""
    status, message = check_spo2(95)
    assert status == "OK"

# ============================================
# BLOOD PRESSURE ALERT TESTS
# ============================================

def test_normal_blood_pressure_returns_ok():
    """Normal blood pressure should return OK"""
    status, message = check_blood_pressure(110, 70)
    assert status == "OK"

def test_high_systolic_returns_warning():
    """Systolic above 120 should return WARNING"""
    status, message = check_blood_pressure(150, 70)
    assert status == "WARNING"

# ============================================
# FULL ALERT CHECK TESTS
# ============================================

def test_normal_patient_has_no_critical_alerts():
    """Normal patient should have no CRITICAL alerts"""
    normal_reading = {
        "heart_rate": 75,
        "spo2": 98,
        "systolic": 110,
        "diastolic": 70
    }
    alerts = check_all_vitals(normal_reading)
    critical_alerts = [a for a in alerts if a["type"] == "CRITICAL"]
    assert len(critical_alerts) == 0

def test_critical_patient_has_critical_alerts():
    """Critical patient should have CRITICAL alerts"""
    dangerous_reading = {
        "heart_rate": 130,
        "spo2": 88,
        "systolic": 150,
        "diastolic": 95
    }
    alerts = check_all_vitals(dangerous_reading)
    critical_alerts = [a for a in alerts if a["type"] == "CRITICAL"]
    assert len(critical_alerts) > 0