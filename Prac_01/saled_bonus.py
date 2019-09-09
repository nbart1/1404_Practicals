"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = 0
while sales >= 0:
    sales = float(input("Enter Sales: $"))
    if sales >= 1000:
        bonus = sales * .15
        print(bonus)
    elif sales > 0:
        bonus = sales * .1
        print(bonus)
print()
