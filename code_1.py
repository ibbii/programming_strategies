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
minimum_downpayment_percentage = float(input(f"Enter down payment percentage (minimum {round(minimum_downpayment_percentage, 3)}): "))
print(f"Down payment amount is ${minimum_downpayment_percentage}") 

if minimum_downpayment_percentage < 10: 
    insurance_premium = 0.04
elif minimum_downpayment_percentage < 15:
    insurance_premium = 0.031
elif minimum_downpayment_percentage < 20:
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

amortization_period = int(input("Enter mortgage amortization period (5, 10, 15, 20, 25)"))

while amortization_period not in (5, 10, 15, 20, 25):
    print ("That is not a acceptable Amortization Period, please select one of the following: 5, 10, 15, 20, 25")
    amortization_period = int(input("What is the amortization period you want?(5, 10, 15, 20, 25)"))

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
#print (f"Effective Monthly Rate / Monthly Payment: {EMR} / {monthly_payment}")
# print (name)
# print (f"Minimum Downpayment / Percentage of House Price: {minimum_downpayment} / {minimum_downpayment_percentage}")
# print (f"Insurance Premium / Insurance Cost: {insurance_premium} / {insurance_cost}")
# print (f"Principal Amount: {principal}") 
