price = int(input('Enter the price of the good(s): '))
if price < 0:
    print('Invalid price (Price of good(s) can\'t be a negative number)')
    exit()
elif price == 0:
    print('The good(s) is not free, please put a valid price')
    exit()
credit_score = int(input('Enter 1 or 2 to know if you have a good credit score: '))
if credit_score == 1:
    ten_percent_discount= 10 * price / 100
    new_price = price - ten_percent_discount
    down_payment = 10 * new_price / 100
    print(f"""
You have a good credit score 
So you are give a 10% discount ({ten_percent_discount}) on your good(s),
Your new price after the discount is ({new_price}).
As a customer with good credit score, You can also make 10% ({down_payment}) down payment of the good(s) price""")
elif credit_score == 2:
    twenty_five_percent = 25 * price / 100
    print(f"you have to make a down payment of 25% ({twenty_five_percent}) of the goods price ")
else:
    print('Invalid number for checking credit score')