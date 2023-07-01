total_miles = 0
total_gallons = 0
while True:
    gallons = float(input('Enter the gallons used (-1 to end): '))
    if gallons == -1:
        print(f'The overall average miles/gallon was {total_miles/total_gallons}')
        exit()
    miles = float(input('Enter the miles driven: '))
    print(f'The miles/gallon for this tank was {miles / gallons}')
    total_gallons += gallons
    total_miles += miles
