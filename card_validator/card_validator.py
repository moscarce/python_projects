def card_number() -> str:
    number = input('Enter card number: ')
    card_length = True
    while (
        not number.isnumeric()
        or len(number) <= 12
        or len(number) >= 17
    ):
        print('Invalid card number')
        number = input('Enter card number: ')

    return number
def card_type(numbers : str)->str:
    if numbers[0] == '4':
        return 'VisaCard'
    elif numbers[0] == '5':
        return 'MasterCard'
    elif numbers[0] == '6':
        return 'Discover Cards'
    elif numbers[0] == '3' and numbers[1] == '7':
        return "AmericanExpressCard"
    else:
        return 'Invalid Card'
def calculate_odd_position(numbers: str) -> int:
    return sum(int(numbers[index]) for index in range(len(numbers) - 1, -1, -2))

def calculate_even_position(numbers:str)->int:
    total = 0
    for index in range(len(numbers)-2,-1,-2):
        digit = int(numbers[index]) * 2
        if digit > 9:
            digit -= 9
        total += digit
    return total
def validate_card(number1: int,number2:int)->str:
    return 'Valid' if (number1 + number2)%10 == 0 else 'Invalid'
def card_details():
    numbers = card_number()
    length = len(numbers)
    type = card_type(numbers)
    status = validate_card(calculate_odd_position(numbers),calculate_even_position(numbers))
    print(f'''
    ************************************************************************************************
    **Credit Card Type: {type}
    **Credit Card Number: {numbers}
    **Credit Card Digit Length: {length}
    **Credit Card Validity Status: {status}
    ************************************************************************************************
    ''')



card_details()
