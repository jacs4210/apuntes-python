price_house = 1000000
is_good_credit = True

if is_good_credit:
    down_payment = price_house * 0.1
else:
    down_payment = price_house * 0.2

print(f"The down payment is: ${down_payment}")