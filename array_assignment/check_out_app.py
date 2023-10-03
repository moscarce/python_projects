import re
import datetime

items_list = []
pieces_list = []
price_list = []
total_price = []
customers_name:str
cashiers_name:str


def customer_name()->str:
    name = input("What is the customer's name?\n")
    while not bool(re.match(r"^[a-zA-Z' ]+$",name)):
        print('Invalid name')
        print('Name can only be in alphabets')
        name = input("What is the customer's name?\n")
    return name


def bought_items()->str:
    goods = input('What did the user buy?\n')
    return goods


def pieces_bought():
    number_of_pieces_bought = input('How many pieces?\n')
    while not number_of_pieces_bought.isnumeric():
        print('Invalid number of pieces')
        number_of_pieces_bought = input('How many pieces?\n')
    return int(number_of_pieces_bought)


def price_per_unit():
    price = input('How much per unit?\n')
    while not bool(re.match(r"^\d+(\.\d+)?$",price)):
        print('Invalid price')
        price = input('How much per unit?\n')
    return int(price)


def update_list():
    items_list.append(bought_items())
    pieces_list.append(pieces_bought())
    price_list.append(price_per_unit())
    add_more()


def cashier_name():
    name = input('What is your name?\n')
    while not bool(re.match(r"^[a-zA-Z' ]+$",name)):
        print('Invalid name')
        name = input('What is your name?\n')
    return name


def calculate_total_price():
    for index in range(len(price_list)):
        answer = price_list[index] * pieces_list[index]
        total_price.append(answer)


def calculate_sub_total(total:list)->int:
    total_sub = 0
    for element in total:
        total_sub += element
    return total_sub


def collect_customer_payment(bill:float)->float:
    amount_paid = input('How much did the user pay?\n')
    while not bool(re.match(r"^\d+(\.\d+)?$",amount_paid)):
        print('Invalid price')
        amount_paid = input('How much did the user pay?\n')
    amount_paid = float(amount_paid)
    if amount_paid > bill:
        return amount_paid
    else:
        print(f'Amount too low\n Kindly pay {bill}')
        return collect_customer_payment(bill)


def collect_and_calculate_discount(total: int)->float:
    collected_discount = input('How much discount will he/she get?\n')
    while not collected_discount.isnumeric():
        print('Invalid discount')
        collected_discount = input('How much discount will he/she get?\n')
    discount_percentage = int(collected_discount)/100
    return discount_percentage * total


def add_more():
    answer = input('Add more items?\n')
    answer = answer.lower()
    match answer:
        case 'yes':
            update_list()
        case 'no':
            pass
        case _ :
            print('Invalid answer')
            add_more()


customers_name = customer_name()
update_list()
cashiers_name = cashier_name()
calculate_total_price()
sub_total = (calculate_sub_total(total_price))
discount = collect_and_calculate_discount(sub_total)
vat = (17.5/100) * sub_total
bill_total = (sub_total - discount) + vat
sub_total = "{:.2f}".format(sub_total)
discount = "{:.2f}".format(discount)
vat = "{:.2f}".format(vat)
formatted_bill_total = "{:.2f}".format(bill_total)
current_datetime = datetime.datetime.now()
formatted_date = current_datetime.strftime("%Y-%m-%d")
formatted_time = current_datetime.strftime("%H:%M:%S")
print(f'''
SEMICOLON STORES
MAIN BRANCH
LOCATION: 312 HERBERT MACAULAY WAY, SABO, YABA, LAGOS.
TEL: 83293828343
Date: {formatted_date} {formatted_time}
Cashier: {cashiers_name}
Customer Name: {customers_name}
========================================================================================
                                    ITEM    QTY     PRICE       TOTAL(NGN)
----------------------------------------------------------------------------------------
''')
for elements in range(len(items_list)):
    print(f'\t\t\t\t\t\t\t {items_list[elements]:<10} \t {pieces_list[elements]:<5}   {price_list[elements]:<5} \t\t {total_price[elements]:<5}')

print(f'''
---------------------------------------------------------------------------------------
                                                Sub Total:      {sub_total}
                                                 Discount:      {discount}
                                             VAT @ 17.50%:      {vat}
=======================================================================================
                                               Bill total:      {formatted_bill_total}
=======================================================================================
                    THIS IS NOT A RECEIPT KINDLY PAY {formatted_bill_total}
=======================================================================================


''')


paid_amount = collect_customer_payment(bill_total)
print(paid_amount)

print(f'''
SEMICOLON STORES
MAIN BRANCH
LOCATION: 312 HERBERT MACAULAY WAY, SABO, YABA, LAGOS.
TEL: 83293828343
Date: {formatted_date} {formatted_time}
Cashier: {cashiers_name}
Customer Name: {customers_name}
========================================================================================
                                    ITEM    QTY     PRICE       TOTAL(NGN)
----------------------------------------------------------------------------------------
''')
for elements in range(len(items_list)):
    print(f'\t\t\t\t\t\t\t {items_list[elements]:<10} \t {pieces_list[elements]:<5}   {price_list[elements]:<5} \t\t {total_price[elements]:<5}')

print(f'''
---------------------------------------------------------------------------------------
                                                Sub Total:      {sub_total}
                                                 Discount:      {discount}
                                             VAT @ 17.50%:      {vat}
=======================================================================================
                                               Bill total:      {formatted_bill_total}
                                              Amount paid:      {paid_amount}
                                                  Balance:      {paid_amount - bill_total}
=======================================================================================
                        THANK YOU FOR YOUR PATRONAGE
=======================================================================================


''')

