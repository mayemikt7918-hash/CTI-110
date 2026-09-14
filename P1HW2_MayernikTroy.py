# Troy Mayernik
# September 13, 2026
# P1HW2 - Travel Budget
# This program calculates travel expenses and the remaining budget.

# Pseudocode:
# 1. Ask the user for their budget.
# 2. Ask for their travel destination.
# 3. Ask for the amount they will spend on gas.
# 4. Ask for the amount they will spend on accommodation.
# 5. Ask for the amount they will spend on food.
# 6. Add all expenses together.
# 7. Subtract the expenses from the budget.
# 8. Display the results.

# Ask the user for their budget
budget = float(input("Enter your budget: "))

# Ask the user for their travel destination
destination = input("Enter your travel destination: ")

# Ask for travel expenses
gas = float(input("Enter amount you will spend on gas: "))
accommodation = float(input("Enter amount you will spend on accommodation: "))
food = float(input("Enter amount you will spend on food: "))

# Add all expenses together
total_expenses = gas + accommodation + food

# Subtract expenses from the budget
remaining_budget = budget - total_expenses

# Display the results
print()
print("Travel Budget Results")
print("----------------------")
print("Destination:", destination)
print("Budget: $", format(budget, ".2f"))
print("Gas: $", format(gas, ".2f"))
print("Accommodation: $", format(accommodation, ".2f"))
print("Food: $", format(food, ".2f"))
print("Total Expenses: $", format(total_expenses, ".2f"))
print("Remaining Budget: $", format(remaining_budget, ".2f"))