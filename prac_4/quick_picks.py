import random

NUMBER_OF_NUMBERS = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    number_of_quick_picks = get_number_of_quick_picks()
    display_quick_picks(number_of_quick_picks)


def get_number_of_quick_picks():
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("Invalid Choice")
        number_of_quick_picks = int(input("How many quick picks? "))
    return number_of_quick_picks


def display_quick_picks(number_of_quick_picks):
    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(NUMBER_OF_NUMBERS):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()
