
# Troy Mayernik
# 10/11/2026
# P3HW2 - Employee Pay
# This program calculates an employee's regular pay, overtime pay, and gross pay.

# Pseudocode:
# Ask the user for the employee's name.
# Ask for hours worked and hourly pay rate.
# If hours worked are greater than 40, calculate overtime hours and pay.
# Otherwise, overtime hours and pay are zero.
# Calculate regular pay and gross pay.
# Display the employee's pay information.

employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked this week: "))
pay_rate = float(input("Enter employee's pay rate: "))

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
    overtime_pay = overtime_hours * pay_rate * 1.5
else:
    overtime_hours = 0
    regular_hours = hours_worked
    overtime_pay = 0

regular_pay = regular_hours * pay_rate
gross_pay = regular_pay + overtime_pay

print("----------------------------------------")
print(f"Employee name: {employee_name}")
print(f"Pay rate: ${pay_rate:.2f}")
print(f"Hours worked: {hours_worked:.1f}")
print(f"Overtime hours: {overtime_hours:.1f}")
print(f"Overtime pay: ${overtime_pay:.2f}")
print(f"Pay for regular hours: ${regular_pay:.2f}")
print(f"Gross pay: ${gross_pay:.2f}")
print("----------------------------------------")
