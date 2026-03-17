# Automated Tests for Vital Signs Simulator
# These tests check that our simulator works correctly
# Just like real medical device testing!

from vital_signs_simulator import generate_heart_rate, generate_spo2, generate_blood_pressure, generate_all_vitals

# ============================================
# HEART RATE TESTS
# ============================================

def test_heart_rate_is_a_number():
    """Heart rate should always be a number"""
    hr = generate_heart_rate()
    assert isinstance(hr, (int, float))

def test_heart_rate_minimum():
    """Heart rate should never go below 60"""
    for i in range(100):  # Test 100 times
        hr = generate_heart_rate()
        assert hr >= 60, f"Heart rate {hr} is too low!"

def test_heart_rate_maximum():
    """Heart rate should never go above 100"""
    for i in range(100):
        hr = generate_heart_rate()
        assert hr <= 100, f"Heart rate {hr} is too high!"

# ============================================
# SpO2 TESTS
# ============================================

def test_spo2_minimum():
    """SpO2 should never go below 95%"""
    for i in range(100):
        spo2 = generate_spo2()
        assert spo2 >= 95, f"SpO2 {spo2} is too low!"

def test_spo2_maximum():
    """SpO2 should never exceed 100%"""
    for i in range(100):
        spo2 = generate_spo2()
        assert spo2 <= 100, f"SpO2 {spo2} is too high!"

# ============================================
# BLOOD PRESSURE TESTS
# ============================================

def test_blood_pressure_systolic_range():
    """Systolic pressure should be between 90-120"""
    for i in range(100):
        systolic, diastolic = generate_blood_pressure()
        assert 90 <= systolic <= 120

def test_blood_pressure_diastolic_range():
    """Diastolic pressure should be between 60-80"""
    for i in range(100):
        systolic, diastolic = generate_blood_pressure()
        assert 60 <= diastolic <= 80

def test_systolic_higher_than_diastolic():
    """Systolic should always be higher than diastolic"""
    for i in range(100):
        systolic, diastolic = generate_blood_pressure()
        assert systolic > diastolic

# ============================================
# FULL SIMULATOR TESTS
# ============================================

def test_generate_all_vitals_returns_correct_count():
    """Should return exactly the number of readings requested"""
    readings = generate_all_vitals(10)
    assert len(readings) == 10

def test_generate_all_vitals_has_all_fields():
    """Each reading should have all required fields"""
    readings = generate_all_vitals(1)
    reading = readings[0]
    assert "timestamp" in reading
    assert "heart_rate" in reading
    assert "spo2" in reading
    assert "systolic" in reading
    assert "diastolic" in reading