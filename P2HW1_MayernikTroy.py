# Troy Mayernik
# September 27, 2026
# P2HW1 - Travel Expenses
# This program calculates travel expenses and displays the remaining budget.

# Pseudocode:
# 1. Ask the user for their budget and travel destination.
# 2. Ask for gas, accommodation, and food expenses.
# 3. Calculate the total expenses.
# 4. Subtract total expenses from the budget.
# 5. Display all results with dollar signs and two decimal places.

budget = float(input("Enter your budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("Enter your gas expense: "))
accommodation = float(input("Enter your accommodation expense: "))
food = float(input("Enter your food expense: "))

total_expenses = gas + accommodation + food
remaining_budget = budget - total_expenses

print("\n------------Travel Expenses------------")
print(f"{'Location:':<22}{destination}")
print(f"{'Initial Budget:':<22}${budget:,.2f}")
print(f"{'Fuel:':<22}${gas:,.2f}")
print(f"{'Accommodation:':<22}${accommodation:,.2f}")
print(f"{'Food:':<22}${food:,.2f}")
print(f"{'Total Expenses:':<22}${total_expenses:,.2f}")
print(f"{'Remaining Balance:':<22}${remaining_budget:,.2f}")
