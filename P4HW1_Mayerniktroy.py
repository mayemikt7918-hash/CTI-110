
# Troy Mayernik
# 10/26/2026
# P4HW1
# This program collects test scores, validates them, drops the lowest score,
# calculates the average, and displays the letter grade.

# Pseudocode:
# 1. Ask the user how many scores they want to enter.
# 2. Create an empty list to store the scores.
# 3. Use a loop to collect each score.
# 4. Check whether each score is between 0 and 100.
# 5. If a score is invalid, display an error and ask again.
# 6. If a score is valid, add it to the score list.
# 7. Find and display the lowest score.
# 8. Remove the lowest score from the list.
# 9. Display the modified score list.
# 10. Calculate and display the average of the modified list.
# 11. Determine and display the letter grade.
# 12. End the program.

# Ask the user how many scores they want to enter
num_scores = int(input("How many scores do you want to enter? "))

# Make sure the number of scores is positive
while num_scores <= 0:
    print("Please enter a number greater than 0.")
    num_scores = int(input("How many scores do you want to enter? "))

# Create an empty list to store valid scores
scores = []

# Loop to collect the scores
for i in range(num_scores):
    score = float(input(f"Enter score #{i + 1}: "))

    # Keep asking until the score is valid
    while score < 0 or score > 100:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{i + 1} again: "))

    # Add the valid score to the list
    scores.append(score)

# Find the lowest score
lowest_score = min(scores)

# Remove one occurrence of the lowest score
scores.remove(lowest_score)

# Calculate the average of the remaining scores
average = sum(scores) / len(scores)

# Determine the letter grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# Display the results
print("\n------------Results------------")
print(f"{'Lowest score  :':<25}{lowest_score:.1f}")
print(f"{'Modified List :':<25}{scores}")
print(f"{'Scores Average:':<25}{average:.2f}")
print(f"{'Grade         :':<25}{grade}")
print("--------------------------------")
