def fibonacci(number:int ):
    num1 = 0
    num2 = 1
    print(f'{num1}\t{num2}',end='\t')
    num = 0
    while num <= number:
        num = num1 + num2
        if num > number: continue
        num1 = num2
        num2 = num
        print(num,end='\t')
    print()

fibonacci(50)

