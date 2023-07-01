def multiplication_table(num):
    for x in range(1,13):
        for t in range(1,num+1):
            print('%i X %i = %-4i' %(t,x, x*t),end='\t\t')
        print()

multiplication_table(9)