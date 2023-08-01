import math
print("Investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on your home loan")
user_inp = input("Enter either 'Investment' or 'bond' from the menu above to proceed: ").upper()
if user_inp == "INVESTMENT":
    deposit = int(input("How much are you depositing?: "))
    rate = int(input("What is the interest rate?: "))
    num_years = int(input("How many years do you plan on investing for?: "))
    interest = input("Do you want simple or compound interest?: ").upper()
    if interest == "SIMPLE":
        total = deposit*(1 + (rate/100)*num_years)
        print("Your total amount after " + str(num_years) + " years is: " + str(round(total,2)))
    elif interest == "COMPOUND":
        total = deposit*math.pow((1+rate/100),num_years)
        print("Your total amount after " + str(num_years) + " years is: " + str(round(total,2)))
    print("Wrong entry try again.")
elif user_inp == "BOND":
    house_value = int(input("What is the present value of the house?: "))
    rate = int(input("What is the interest rate?: "))/100
    num_months = int(input("How many months do you plan on taking to repay the bond?: "))
    repayment = ((rate/12) * house_value)/(1-(1+(rate/12))**(-num_months))
    print("You will have to pay " + str(round(repayment,2)) + (" every month"))
print("Wrong entry try again.")

    
    




