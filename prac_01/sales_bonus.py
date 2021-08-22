"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
UNDER_THOUSAND_BONUS = 0.1
THOUSAND_AND_OVER_BONUS = 0.15

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = UNDER_THOUSAND_BONUS
    else:
        bonus = THOUSAND_AND_OVER_BONUS
    print(f"You bonus is {sales * bonus}")
    sales = float(input("Enter sales: $"))
