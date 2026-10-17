# Electricity Bill

# Rate per unit
# First 100 units =   3.0
# Next 200 units (101 to 300) =   5.0
# Above 300 units = 8.0

# Bill = energy charge + fixed charge + surcharge,
# fixed charge is 50 //  surcharge is 5% of the energy charge.

unit = float(input("Enter total Units : "))

if unit < 0:
    print("Fuck you")

elif unit <= 100:
    bill = (unit * 3)

elif unit <= 300:
    bill = (100 * 3)    +   ((unit - 100) * 5)       # for 100 + them remaining + 50 + 5%

else:
    bill = ((100 * 3) + (200 * 5) + ((unit - 300) * 8))  # for 100 + them remaining + 50 + 5%

sur_charge = (bill * 5 ) / 100
fixed_charge = 50
total_payable_amt = bill + fixed_charge + sur_charge

print("Units : ", unit)
print(" Payable amt. : ", bill)
print(" SurCharge : ", sur_charge)
print(" Fixed Charge : ", fixed_charge)
print(" Total Payable Amt. : ",total_payable_amt)
