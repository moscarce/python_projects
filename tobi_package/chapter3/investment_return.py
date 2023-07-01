for years in range(1,30):
    rate = (1 + 0.07)**years
    amount = rate * 1000
    print(f'Investment return on $1000 for {years} year(s) = ${amount}')