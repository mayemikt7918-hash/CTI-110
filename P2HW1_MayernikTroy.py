# Troy Mayernik
# September 27, 2026
# P2HW1
# This program calculates the total expenses for a trip and subtracts them from the travel budget.

budget = float(input("Enter your budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("Enter your gas expense: "))
accommodation = float(input("Enter your accommodation expense: "))
food = float(input("Enter your food expense: "))
total_expenses = gas + accommodation + food
remaining_budget = budget - total_expenses
print("Travel destination:", destination)
print("Total expenses:", total_expenses)
print("Remaining budget:", remaining_budget)
