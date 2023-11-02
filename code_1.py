house_price = float(input("What is the price of the house you are planning on purchasing?"))

if house_price <= 500000:
    minimum_downpayment = house_price * 0.05
elif house_price <= 1000000:
    minimum_downpayment = (500000 * 0.05) + ((house_price - 500000) * 0.1) 
else: 
    minimum_downpayment = house_price * 0.2

minimum_downpayment_percentage = minimum_downpayment / house_price

if minimum_downpayment_percentage < 0.1: 
    insurance_premium = 0.04
elif minimum_downpayment_percentage < 0.15:
    insurance_premium = 0.031
elif minimum_downpayment_percentage < 0.2:
    insurance_premium = 0.028
else:
    insurance_premium = 0

insurance_cost = (house_price - minimum_downpayment) * insurance_premium 

principal = house_price - minimum_downpayment + insurance_cost

amortization_period = int(input("What is the amortization period you want?(5, 10, 15, 20, 25)"))

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

monthly_payment = principal * ((EMR * ((1 + EMR)**months))/ (((1 + EMR)**months) - 1))

print (f"House price: {house_price}") 
print (f"Minimum Downpayment / Percentage of House Price: {minimum_downpayment} / {minimum_downpayment_percentage}")
print (f"Insurance Premium / Insurance Cost: {insurance_premium} / {insurance_cost}")
print (f"Principal Amount: {principal}") 
print (f"Effective Monthly Rate / Monthly Payment: {EMR} / {monthly_payment}")