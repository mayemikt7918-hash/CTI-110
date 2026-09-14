# Troy Mayernik
# September 13, 2026
# P1HW1
# This program collects integer values from the user and performs
# exponentiation and addition/subtraction calculations.

print("-----Calculating Exponents-----")

base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))

result = base ** exponent

print()
print(f"{base} raised to the power of {exponent} is {result} !!")

print()
print("-----Addition and Subtraction-----")

num1 = int(input("Enter an integer: "))
num2 = int(input("Enter an integer: "))
num3 = int(input("Enter an integer: "))

result2 = num1 + num2 - num3

print()
print(f"{num1} + {num2} - {num3} is {result2} !!")