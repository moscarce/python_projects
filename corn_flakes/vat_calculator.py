def your_vat():
    amount = 0
    vat = 0
    count = 0
    while count < 3:
        if count == 0:
            price = input('Enter price: ')
            if price.isnumeric() and (int(price) > 0):
                amount = int(price)
                count += 1
                continue
            print('Invalid price')
        if count == 1:
            vat_charge = input('Enter vat: ')
            if vat_charge.isnumeric() and (int(vat_charge) > 0):
                vat = int(vat_charge)/100 * amount
                count += 1
                continue
            print('Invalid vat')
        if count == 2:
            return amount + vat


print(your_vat())
