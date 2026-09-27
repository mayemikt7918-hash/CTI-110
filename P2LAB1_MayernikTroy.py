# Troy Mayernik
# September 27, 2026
# P2LAB1
# This program calculates the diameter, circumference, and area of a circle.

# Pseudocode:
# Get the radius from the user
# Calculate the diameter
# Calculate the circumference
# Calculate the area
# Display the results with the required decimal places

import math

radius = float(input("What is the radius of the circle? "))

diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print(f"Diameter: {diameter:.1f}")
print(f"Circumference: {circumference:.2f}")
print(f"Area: {area:.3f}")