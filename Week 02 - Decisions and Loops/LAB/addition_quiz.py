
"""
Step 1: Generate two single-digit integers for number1 (e.g., 4) and number2 (e.g., 5)
Step 2: Prompt the student to answer, "What is 4 + 5?" (user input)
Step 3: Check if the student's answer is correct.
"""
import random

while True:
    number1 = random.randint(50, 100)
    number2 = random.randint(50, 100)

    answer = int(input(f"What is {number1} + {number2}? "))

    if answer == (number1 + number2):
        print("Correct!")
        break
    else:
        print("Try again.")