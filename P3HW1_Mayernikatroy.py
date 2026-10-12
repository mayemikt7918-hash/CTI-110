
# Troy Mayernik
# 10/11/2026
# P3HW1 - Debugging
# This program calculates the lowest, highest, sum, and average
# of six grades and determines the letter grade.

# Pseudocode:
# Ask the user to enter six grades.
# Store the grades in a list.
# Find the lowest and highest grades.
# Calculate the sum and average.
# Determine the letter grade.
# Display the results.

grades = []

for i in range(1, 7):
    grade = float(input(f"Enter grade #{i}: "))
    grades.append(grade)

lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)

if average >= 90:
    letter_grade = "A"
elif average >= 80:
    letter_grade = "B"
elif average >= 70:
    letter_grade = "C"
elif average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print()
print("------------Results------------")
print(f"Lowest Grade:    {lowest:.1f}")
print(f"Highest Grade:   {highest:.1f}")
print(f"Sum of Grades:   {total:.1f}")
print(f"Average:         {average:.2f}")
print(f"Letter Grade:    {letter_grade}")
print("--------------------------------")
