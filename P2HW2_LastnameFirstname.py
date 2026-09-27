#Your Name
#09/27/2026
#P2HW2 - List
#This program asks the user to enter six module grades,
#stores the grades in a list, and calculates the lowest,
#highest, sum, and average of the grades.

"""
Pseudocode:
1. Ask the user to enter the grade for Module 1.
2. Ask the user to enter the grade for Module 2.
3. Ask the user to enter the grade for Module 3.
4. Ask the user to enter the grade for Module 4.
5. Ask the user to enter the grade for Module 5.
6. Ask the user to enter the grade for Module 6.
7. Store all six grades in a list.
8. Find the lowest grade.
9. Find the highest grade.
10. Find the sum of the grades.
11. Find the average of the grades.
12. Display the results.
"""

module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

grades = [module1, module2, module3, module4, module5, module6]

lowest_grade = min(grades)
highest_grade = max(grades)
sum_grades = sum(grades)
average_grade = sum_grades / len(grades)

print()
print("----------Results----------")
print(f"Lowest Grade: {lowest_grade:.1f}")
print(f"Highest Grade: {highest_grade:.1f}")
print(f"Sum of Grades: {sum_grades:.1f}")
print(f"Average: {average_grade:.2f}")
