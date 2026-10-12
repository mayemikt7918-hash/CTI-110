
# Troy Mayernik
# 10/11/2026
# P3LAB - Calculate Dollars and Coins
# This program calculates the fewest dollars and coins needed for an amount of money.

# Pseudocode:
# Ask the user to enter an amount of money.
# Convert the amount to cents.
# Calculate the number of dollars.
# Calculate the remaining quarters, dimes, nickels, and pennies.
# Display only denominations that are needed.
# Use singular names for one and plural names for more than one.

money = float(input("Enter the amount of money as a float: "))

cents = int(round(money * 100))

dollars = cents // 100
cents = cents - dollars * 100

quarters = cents // 25
cents = cents - quarters * 25

dimes = cents // 10
cents = cents - dimes * 10

nickels = cents // 5
cents = cents - nickels * 5

pennies = cents

if dollars > 0:
    if dollars == 1:
        print("1 dollar")
    else:
        print(f"{dollars} dollars")

if quarters > 0:
    if quarters == 1:
        print("1 quarter")
    else:
        print(f"{quarters} quarters")

if dimes > 0:
    if dimes == 1:
        print("1 dime")
    else:
        print(f"{dimes} dimes")

if nickels > 0:
    if nickels == 1:
        print("1 nickel")
    else:
        print(f"{nickels} nickels")

if pennies > 0:
    if pennies == 1:
        print("1 penny")
    else:
        print(f"{pennies} pennies")