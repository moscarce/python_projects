total_score = 0
for x in range(20):
    score = int(input('Enter student score : '))
    total_score = total_score + score
average_score = total_score / 20
print(f'''
******************************************************************
            Aso Rock Secondary School, Abuja Nigeria
******************************************************************
Class: SSS 3
Number of Student in class: {20}
Total score: {total_score}
Average Score: {average_score}
******************************************************************
''')
