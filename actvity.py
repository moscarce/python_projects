# for number in range(1, 11):
#     print(number, end=' ')

if __name__ == '__main__':
    n = int(input().strip())
if (n % 2 == 1) or ((n % 2 == 0) and (n > 5 and n < 21)):
    print("Weird")
elif ((n % 2 == 0)and((n > 1 and n < 6) or (n > 20))):
    print("Not Weird")