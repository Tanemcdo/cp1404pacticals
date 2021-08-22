"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    score = float(input("Enter score: "))
    result = categorise_score(score)
    print(result)
    random_score = random.randint(0, 100)
    result = categorise_score(random_score)
    print(result)


def categorise_score(score):
    if score < 0 or score > 100:
        return "Invalid Score"
    elif score > 90:
        return"Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"


main()
