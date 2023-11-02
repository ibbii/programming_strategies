name = input("Enter client name: ")
address = input("Enter address of property: ")
house_price = float(input("Enter purchase price: "))

if house_price <= 500000:
    minimum_downpayment = house_price * 0.05
elif house_price <= 1000000:
    minimum_downpayment = (500000 * 0.05) + ((house_price - 500000) * 0.1) 
else: 
    minimum_downpayment = house_price * 0.2



downpayment_percentage = (minimum_downpayment / house_price * 100) 
downpayment = ((float(input(f"Enter down payment percentage (minimum {downpayment_percentage:.3f}): ")) / 100) * house_price) 

print(f"Down payment amount is ${downpayment}") 

if downpayment_percentage < 10: 
    insurance_premium = 0.04
elif downpayment_percentage < 15:
    insurance_premium = 0.031
elif downpayment_percentage < 20:
    insurance_premium = 0.028
else:
    insurance_premium = 0

insurance_cost = (house_price - minimum_downpayment) * insurance_premium 
print(f"Mortgage insurance price is {insurance_cost}")

principal = house_price - minimum_downpayment + insurance_cost
print(f"Total mortgage amount is ${principal}")

mortgage_term = int(input("Enter mortgage term (1, 2, 3, 5, 10): "))

while mortgage_term not in (1, 2, 3, 5, 10):
    print ("That is not a acceptable mortgage term, please select one of the following: 1, 2, 3, 5, 10")
    mortgage_term = int(input("Enter mortgage term (1, 2, 3, 5, 10):"))

amortization_period = int(input("Enter mortgage amortization period (5, 10, 15, 20, 25): "))

while amortization_period not in (5, 10, 15, 20, 25):
    print ("That is not a acceptable Amortization Period, please select one of the following: (5, 10, 15, 20, 25): ")
    amortization_period = int(input("What is the amortization period you want?(5, 10, 15, 20, 25): "))

if amortization_period == 5:
    mortgage_term = 1
    mortgage_rate = 0.0595
elif amortization_period ==10: 
    mortgage_term = 2
    mortgage_rate = 0.059
elif amortization_period ==15:
    mortgage_term = 3
    mortgage_rate = 0.056
elif amortization_period ==20:
    mortgage_term = 5
    mortgage_rate = 0.0529
else:
    mortgage_term = 10
    mortgage_rate = 0.06

EMR = ((1 + (mortgage_rate / 2))**2)**(1/12) - 1

months = 12* amortization_period 

monthly_payment = "{:2f}".format(principal * ((EMR * ((1 + EMR)**months))/ (((1 + EMR)**months) - 1)))

print(f"Interest rate for thr term will be {EMR}%")
print(f"Monthly payment amount is: ${monthly_payment}")

months = 12 * amortization_period

# Calculate monthly payment
monthly_payment = principal * (EMR * (1 + EMR) ** months) / ((1 + EMR) ** months - 1)

print(f"Interest rate for the term will be {EMR * 100:.2f}%")
print(f"Monthly payment amount is: ${monthly_payment:.2f}")

amort_schedule = input("Would you like to see the amortization schedule? (Y/N): ").upper()
if amort_schedule == "Y":
    print("             \nAmortization Schedule:") # Calculate and print the amortization schedule
    print("Month  Opening Balance  Monthly Payment  Monthly Principal  Monthly Interest  Closing Balance")

    opening_balance = principal
    for month in range(1, months + 1):
        monthly_interest = opening_balance * EMR
        monthly_principal = monthly_payment - monthly_interest
        closing_balance = opening_balance - monthly_principal
    
        print(f"{month:3}  ${opening_balance:.2f}  ${monthly_payment:.2f}  ${monthly_principal:.2f}  ${monthly_interest:.2f}  ${closing_balance:.2f}")
    
        opening_balance = closing_balance
else:
    print("Thank you, goodbye")

 
