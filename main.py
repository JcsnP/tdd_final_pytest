from function_calculate_salary import calculate_salary

working_day = int(input("please input working day: "))
total_ot = int(input("please input total ot hour: "))
late_day = int(input("please input late day: "))

result = calculate_salary(working_day, total_ot, late_day)
print(result)