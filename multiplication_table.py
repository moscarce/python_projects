def multiplication_table(num):
    if num < 1:
        print('please use a positive integer that is greater than ')
    for x in range(1,13):
        for t in range(1,num+1):
            print('%i X %i = %-4i' %(t,x, x*t),end='\t\t')
        print()


multiplication_table(10)
