# 63102230 Chitsanupong Paenyoi
# input => จำนวนวันทำงาน, จำนวน ot รวม, จำนวนวันมาสาย

from function_calculate_salary import calculate_salary
import pytest

# days 32
@pytest.mark.validate
def test_working_day_32_total_ot_0_late_day_0():
  working_day = 32
  total_ot = 0
  late_day = 0
  expected_result = "invalid day"
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result

# days -1
@pytest.mark.validate
def test_working_day_minus_1_total_ot_0_late_day_0():
  working_day = -1
  total_ot = 0
  late_day = 0
  expected_result = "invalid day"
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result

# total op -1
@pytest.mark.validate
def test_working_day_minus_1_total_ot_minus_1_late_day_0():
  working_day = 0
  total_ot = -1
  late_day = 0
  expected_result = "invalid total ot"
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result

# total op more than maximum
# 1 day, max ot is 180, in 1 month (31 days) max ot is 93
@pytest.mark.validate
def test_working_day_0_total_ot_94_late_day_0():
  working_day = 0
  total_ot = 94
  late_day = 0
  expected_result = "number of OTs above threshold per day"
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result

# late day < 0
@pytest.mark.validate
def test_working_day_0_total_ot_0_late_day_minus_1():
  working_day = 0
  total_ot = 0
  late_day = -1
  expected_result = "invalid late day"
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result

# late day > 31
@pytest.mark.validate
def test_working_day_0_total_ot_0_late_day_32():
  working_day = 0
  total_ot = 0
  late_day = 32
  expected_result = "invalid late day"
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result

# number of OTs above threshold per day
@pytest.mark.validate
def test_working_day_1_total_ot_5_late_day_0():
  working_day = 1
  total_ot = 5
  late_day = 0
  expected_result = "number of OTs above threshold per day"
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result

# normal test, max, has invalid late day
@pytest.mark.validate
def test_working_day_31_total_ot_93_late_day_minus_1():
  working_day = 31
  total_ot = 93
  late_day = -1
  expected_result = "invalid late day"
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result

# invalid total ot and late day
# total ot should invalid first
@pytest.mark.validate
def test_working_day_31_total_ot_minus_3_late_day_minus_1():
  working_day = 31
  total_ot = -3
  late_day = -1
  expected_result = "invalid total ot"
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result

# input working day as string
@pytest.mark.validate
def test_working_day_str_31_total_ot_0_late_day_0():
  working_day = "31"
  total_ot = 0
  late_day = 0
  expected_result = "please input as integet"
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result

# input working day as string
@pytest.mark.validate
def test_working_day_0_total_ot_str_64_late_day_0():
  working_day = 0
  total_ot = "64"
  late_day = 0
  expected_result = "please input as integet"
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result

# input late day as string
@pytest.mark.validate
def test_working_day_0_total_ot_0_late_day_str_15():
  working_day = 0
  total_ot = 0
  late_day = "15"
  expected_result = "please input as integet"
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result

# input late day as string
@pytest.mark.validate
def test_working_day_float_20_2_total_ot_4_late_day_15():
  working_day = 20.2
  total_ot = 4
  late_day = 15
  expected_result = "please input as integet"
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result

# input late day as string
@pytest.mark.validate
def test_working_day_float_20_2_total_ot_str_4_late_day_15():
  working_day = 20.2
  total_ot = "4"
  late_day = 15
  expected_result = "please input as integet"
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result

# input late day as string
@pytest.mark.validate
def test_working_day_float_20_2_total_ot_str_4_late_day_float_15_4():
  working_day = 20.2
  total_ot = "4"
  late_day = 15.4
  expected_result = "please input as integet"
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result

# input late day as string
@pytest.mark.validate
def test_total_ot_hour_more_than_woking_day__working_day_20_total_ot_70_late_day_0():
  working_day = 20
  total_ot = 70
  late_day = 0
  expected_result = "number of OTs above threshold per day"
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result

# all inputs is zero
@pytest.mark.validate
def test_working_day_0_total_ot_0_late_day_0():
  working_day = 0
  total_ot = 0
  late_day = 0
  expected_result = 0
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result

# normal test
@pytest.mark.display
def test_working_day_minus_1_total_ot_minus_1_late_day_minus_1():
  working_day = -1
  total_ot = -1
  late_day = -1
  expected_result = "all input are invalid"
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result

# normal test
@pytest.mark.display
def test_working_day_1_total_ot_0_late_day_0():
  working_day = 1
  total_ot = 0
  late_day = 0
  expected_result = 340
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result
  
# normal test, min
@pytest.mark.display
def test_working_day_1_total_ot_1_late_day_0():
  working_day = 1
  total_ot = 3
  late_day = 0
  expected_result = 520
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result

# normal test, min
@pytest.mark.display
def test_working_day_1_total_ot_1_late_day_1():
  working_day = 1
  total_ot = 3
  late_day = 1
  expected_result = 520
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result

# normal test, max
@pytest.mark.display
def test_working_day_31_total_ot_93_late_day_0():
  working_day = 31
  total_ot = 93
  late_day = 0
  expected_result = 17120
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result

# normal test, max, has late day
@pytest.mark.display
def test_working_day_31_total_ot_93_late_day_1():
  working_day = 31
  total_ot = 93
  late_day = 1
  expected_result = 16120
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result

# normal test, max, has late day
@pytest.mark.display
def test_working_day_15_total_ot_45_late_day_15():
  working_day = 15
  total_ot = 45
  late_day = 15
  expected_result = 7800
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result