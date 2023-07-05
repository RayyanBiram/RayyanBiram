import math

finance_choice = input('''
Investment - to calculate the amount of interest you'll earn on your investment
Bond       - to calculate the amount you'll have to pay on a home loan

Enter either 'investment' or 'bond' from the menu above to proceed: ''')

finance_choice = finance_choice.lower()

if finance_choice != "investment" and finance_choice != "bond":
    print("Invalid Input. You have not typed either 'investment' or 'bond'")

elif finance_choice == "investment":
    money = float(input("Enter the amount of money to deposit: "))
    interest_rate = float(input("Enter the interest rate (e.g. 8): "))
    years = float(input("Enter the number of years you plan on investing: "))
    interest = input("Enter either 'simple' or 'compound' interest: ")

    if interest == "simple":
        total = (money) * (1 + ((interest_rate / 100) * years))
        print(total)

    elif interest == "compound":
        total = money * math.pow((1 + interest_rate), years)
        print(total)

elif finance_choice == "bond":
    value = float(input("Enter the value of the house (e.g. 100000): "))
    interest_rate = float(input("Enter the interest rate (e.g. 7): "))
    months = float(input("Enter the number of months you plan to take to repay the bond (e.g. 120): "))

    repayment = ((interest_rate / 12) * value) / (1 - (1 + interest_rate) ** (-months))
    print(repayment)