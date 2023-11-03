name = input("Enter client name: ")
address = input("Enter address of property: ")
house_price = float(input("Enter purchase price: "))

if house_price <= 500000:

    minimum_downpayment = house_price * 0.05

elif house_price <= 1000000:

    minimum_downpayment = (500000 * 0.05) + ((house_price - 500000) * 0.1) 

else: 

    minimum_downpayment = house_price * 0.2

minimum_downpayment_percentage = (minimum_downpayment / house_price * 100) 

downpayment_percentage = float(input(f"Enter down payment percentage (minimum {minimum_downpayment_percentage:.3f}): "))
while downpayment_percentage > 100 or downpayment_percentage < minimum_downpayment_percentage:
    print(f"Must be between {minimum_downpayment_percentage} and 100")
    downpayment_percentage = float(input(f"Enter down payment percentage (minimum {minimum_downpayment_percentage:.3f}): "))

downpayment = (downpayment_percentage / 100) * house_price 

print(f"Down payment amount is ${round(downpayment)}") 

if downpayment_percentage < 10: 

    insurance_premium = 4

elif downpayment_percentage < 14:

    insurance_premium = 3.1

elif downpayment_percentage < 19:

    insurance_premium = 2.8

else:
    insurance_premium = 0

insurance_cost = (house_price - downpayment) * (insurance_premium / 100) 

print(f"Mortgage insurance price is {round(insurance_cost)}")

principal = house_price - downpayment + insurance_cost

print(f"Total mortgage amount is ${round(principal)}")

mortgage_term = int(input("Enter mortgage term (1, 2, 3, 5, 10): "))

while mortgage_term not in (1, 2, 3, 5, 10):

    print ("That is not a acceptable mortgage term, please select one of the following: 1, 2, 3, 5, 10")

    mortgage_term = int(input("Enter mortgage term (1, 2, 3, 5, 10):"))

amortization_period = int(input("Enter mortgage amortization period (5, 10, 15, 20, 25): "))

while amortization_period not in (5, 10, 15, 20, 25): 

    print ("That is not a acceptable Amortization Period, please select one of the following: 5, 10, 15, 20, 25")

    amortization_period = int(input("What is the amortization period you want?(5, 10, 15, 20, 25): "))

if  mortgage_term == 1:
    mortgage_rate = 0.0595

elif mortgage_term == 2:
    mortgage_rate = 0.059

elif mortgage_term == 3:
    mortgage_rate = 0.056

elif mortgage_term == 5:
    mortgage_rate = 0.0529
else:
    mortgage_rate = 0.06

EMR = ((1 + mortgage_rate / 2)**2)**(1/12) - 1

month_payment = 12 * amortization_period

# Calculate monthly payment
monthly_payment = principal * (EMR * (1 + EMR) ** month_payment) / (((1 + EMR) ** month_payment) - 1)

print(f"Interest rate for the term will be {mortgage_rate * 100:.2f}%")

print(f"Monthly payment amount is: ${round(monthly_payment)}")

months = 12 * mortgage_term

amort_schedule = input("Would you like to see the amortization schedule? (Y/N): ").upper()

if amort_schedule == "Y":

    print("             Amortization Schedule \n") 
    
    # Calculate and print the amortization schedule
    print("Month  Opening Balance  Monthly Payment  Monthly Principal  Monthly Interest  Closing Balance")

    opening_balance = principal

    add_prince = 0

    add_inter = 0

    for month in range(1, months + 1):
        
        monthly_interest = opening_balance * EMR

        monthly_principal = monthly_payment - monthly_interest

        closing_balance = opening_balance - monthly_principal

        add_prince = add_prince + monthly_principal

        add_inter = add_inter + monthly_interest

        print(f"{month:>3}  {opening_balance:>17.2f}  {monthly_payment:>15.2f}  {monthly_principal:>17.2f}  {monthly_interest:>16.2f}  {closing_balance:>15.2f}")
    
        opening_balance = closing_balance
    print("=" * 95)    
    print(f"Total {add_prince:>52.2f} {add_inter:>17.2f}")
else:

    print("Thank you, goodbye")
