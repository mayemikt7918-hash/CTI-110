# Your Name
# 09/27/2026
# P2LAB2 - Dictionary
# This program uses a dictionary to store automobile MPG values,
# asks the user to select a vehicle and enter miles driven,
# and calculates the gallons of gas needed.

# Pseudocode:
# Create a dictionary containing vehicle names and MPG values.
# Get all keys from the dictionary.
# Display the vehicle keys.
# Ask the user to enter a vehicle.
# Display the MPG for the selected vehicle.
# Ask the user to enter the number of miles they will drive.
# Calculate gallons needed by dividing miles by MPG.
# Display the gallons needed rounded to two decimal places.

cars = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

keys = cars.keys()

print(keys)

vehicle = input("Enter a vehicle to see its MPG: ")

print(f"{vehicle} MPG: {cars[vehicle]}")

miles = float(input("Enter the number of miles you will drive: "))

gallons = miles / cars[vehicle]
print(f"Gallons of gas needed: {gallons:.2f}")
