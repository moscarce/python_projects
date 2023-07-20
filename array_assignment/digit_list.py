def digit_list(number: int):
    result = []
    while number > 0:
        digit = number % 10
        number //= 10
        result.append(digit)
    print(result[::-1])


digit_list(2342)