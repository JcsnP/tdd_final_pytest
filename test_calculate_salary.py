# 63102230 Chitsanupong Paenyoi
# input => จำนวนวันทำงาน, จำนวน ot รวม, จำนวนวันมาสาย

from calculate_salary import calculate_salary

# all inputs is zero
def test_working_day_0_total_ot_0_late_day_0():
  working_day = 0
  total_ot = 0
  late_day = 0
  expected_result = "invalid all inputs"
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result


# days 32
def test_working_day_32_total_ot_0_late_day_0():
  working_day = 32
  total_ot = 0
  late_day = 0
  expected_result = "invalid day"
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result

# days -1
def test_working_day_minus_1_total_ot_0_late_day_0():
  working_day = -1
  total_ot = 0
  late_day = 0
  expected_result = "invalid day"
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result

# total op -1
def test_working_day_minus_1_total_ot_minus_1_late_day_0():
  working_day = 0
  total_ot = -1
  late_day = 0
  expected_result = "invalid total ot"
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result

# total op more than maximum
# 1 day, max ot is 180, in 1 month (31 days) max ot is 93
def test_working_day_0_total_ot_94_late_day_0():
  working_day = 0
  total_ot = 94
  late_day = 0
  expected_result = "number of OTs above threshold per day"
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result

# late day < 0
def test_working_day_0_total_ot_0_late_day_minus_1():
  working_day = 0
  total_ot = 0
  late_day = -1
  expected_result = "invalid late day"
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result

# late day > 31
def test_working_day_0_total_ot_0_late_day_32():
  working_day = 0
  total_ot = 0
  late_day = 32
  expected_result = "invalid late day"
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result

# normal test
def test_working_day_1_total_ot_0_late_day_0():
  working_day = 1
  total_ot = 0
  late_day = 0
  expected_result = 340
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result

# number of OTs above threshold per day
def test_working_day_1_total_ot_5_late_day_0():
  working_day = 1
  total_ot = 5
  late_day = 0
  expected_result = "number of OTs above threshold per day"
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result
  
# normal test, min
def test_working_day_1_total_ot_1_late_day_0():
  working_day = 1
  total_ot = 3
  late_day = 0
  expected_result = 520
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result

# normal test, min
def test_working_day_1_total_ot_1_late_day_1():
  working_day = 1
  total_ot = 3
  late_day = 1
  expected_result = 520
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result

# normal test, max
def test_working_day_31_total_ot_93_late_day_0():
  working_day = 31
  total_ot = 93
  late_day = 0
  expected_result = 17120
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result

# normal test, max, has late day
def test_working_day_31_total_ot_93_late_day_1():
  working_day = 31
  total_ot = 93
  late_day = 1
  expected_result = 16120
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result

# normal test, max, has invalid late day
def test_working_day_31_total_ot_93_late_day_minus_1():
  working_day = 31
  total_ot = 93
  late_day = -1
  expected_result = "invalid late day"
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result

# invalid total ot and late day
# total ot should invalid first
def test_working_day_31_total_ot_minus_3_late_day_minus_1():
  working_day = 31
  total_ot = -3
  late_day = -1
  expected_result = "invalid total ot"
  actual_result = calculate_salary(working_day, total_ot, late_day)
  assert expected_result == actual_result