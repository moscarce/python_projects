student_number = 1
total_score = 0
while True:
    score = int(input('Enter student score : '))
    if student_number < 20:
        total_score = total_score + score
        student_number += 1
    else:
        total_score = total_score + score
        average_score = total_score / student_number
        print('''
        ******************************************************************
                    Aso Rock Secondary School, Abuja Nigeria
        ******************************************************************
        Class: SSS 3
        Number of Student in class:''', student_number,'''
        Total score:''', total_score,'''
        Average Score:''', average_score,'''
        ******************************************************************''')
        exit()