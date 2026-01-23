#Valoracion de trabajo
# 0 = no trabajo ese dia
# Negativo = invalido y debe ser ignorado
# Mayor a 8 hora extra (overtime)
# Mayor a 10 : stop processing
num_data = [8, 7, -1, 9, 0, 6, 10]
days_worked_valid = 0
total_hours = 0
days_overtime = 0
for number in num_data:
    if type(number) ==int or type(number) == float:
        if number < 0:
            print(f"Invalid data {number}, skipping entry.")
            continue
        if number > 10:
            print("Overwork detected, stopping processing.")
            break
        if number > 8:
            days_overtime += 1
            total_hours += number
            days_worked_valid += 1
            print(f"Overtime work recorded: {number} hours.")
        elif number == 0:
            days_worked_valid += 1
            print("No work recorded, valid day with 0 hours.")
        else:
            total_hours += number
            days_worked_valid += 1
            print(f"Regular work recorded: {number} hours.")
            
print(f"""
Results:    
-------------------------
Total valid work days: {days_worked_valid}          
Total hours worked: {total_hours} hours
Total overtime days: {days_overtime} days   """)