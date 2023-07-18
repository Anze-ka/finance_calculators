import math
# A program allows the user to access two different financial calculators:
# an investment calculator and a home loan repayment calculator.

print("investment - \tto calculate the amount of interest you'll earn on your investment")
print ("bond - \t\tto calculate the amount you'll have to pay on a home loan\n")

calculator = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").capitalize() # User enters the calculator type.

if calculator == "Investment":
# Simple Interest Formula: P *(1 + r*t).
# Compound Interest Formula: P * math.pow((1+r),t).
    deposit_amount = float(input("\nHow much money do you consider to deposit? \t\t"))  # User enters 'P' value, known as the amount that the user deposits.
    user_interest_rate1 = float(input("Please enter your interest rate as a percentage (%): \t")) # User enters their interest rate as %.
    user_interest_convert = user_interest_rate1 / 100    # Calculating 'r' value, the interest entered above divided by 100.
    years_invest = int(input("How many years do you plan on investing? \t\t"))    # User enters 't' value, known as a number of years that the money is being invested.
    interest = input("\nDo you prefer 'simple' or 'compound' interest? Please enter: \t")
    if interest == "Simple":
        simple_int_applied = deposit_amount * (1 + (user_interest_convert * years_invest))  # Calculating the amount that the user will receive once the simple interest has been applied, using the formula above.
        print(f"\nYou will get back: {math.ceil(simple_int_applied)}")
    elif interest == "Compound":
        compound_int_applied = deposit_amount * math.pow((1 + user_interest_convert), years_invest) # Calculating the amount that the user will receive once the simple interest has been applied, using the formula above.
        print(f"\nYou will receive back: {math.ceil(compound_int_applied)}")
elif calculator == "Bond":
# Bond Repayment Formula: repayment = (i * P)/(1 - (1 + i)**(-n))
    house_value = int(input("\nWhat is the current value of your house? \t\t")) # User enters 'P' value, known as the value of the house.
    user_interest_rate2 = float(input("Please enter your interest rate as a percentage (%): \t"))  # User enters their interest rate as %.
    user_interest_convert2 = user_interest_rate2 / 100    # The interest rate entered above divided by 100.
    user_monthly_rate = user_interest_convert2 / 12     # Calculating 'i' value, known as the user's interest rate per month.
    months_repay = int(input("How many months do you plan to take to repay the bond? \t")) # User enters ‘n’ value, known as the number of months over which the bond will be repaid.
    repayment = (user_monthly_rate * house_value)/(1 - (1 + user_monthly_rate)**( - months_repay))    # Calculating monthly repayment amount using the above formula.
    print(f"\nEach month you will have to repay: {math.ceil(repayment)}")

elif calculator != "Investment" or calculator != "Bond":    # If the user doesn’t type in a valid calculator type.
    print(f"\n'{calculator}' could not be found in the menu above.\nPlease enter either 'investment' or 'bond'.")
    



