import re
import time

def print_saved_successfully():
    text = '>' * 50
    print('Saving ', end='')
    for char in text:
        print(char, end='')
        time.sleep(0.01)
    print()
    print('Saved successfully')
def collect_student_size()->int:
    student_size = input('How many student do you have? ')
    while not student_size.isnumeric():
        print('Invalid student size')
        student_size = input('How many student do you have? ')
    return int(student_size)


def collect_subject_size():
    subject_size = input('How many subject do they offer? ')
    while not subject_size.isnumeric():
        print('Invalid subject size')
        subject_size = input('How many subject do they offer? ')
    print_saved_successfully()
    return int(subject_size)


def create_student_table()->list:
    student_size = collect_student_size()
    student_list = []
    for lst in range(student_size):
        student_list.append([f'Student {lst+1}'])
    return student_list


def create_subject_list()->list:
    size = collect_subject_size() + 1
    subject_list = ['STUDENT']
    for index in range(1,size):
        subject_list.append(f'SUB{index}')
    subject_list = subject_list + ['TOT','AVE','POS']
    return subject_list


def merge_list()->list:
    student_list = create_student_table()
    subject_list = [create_subject_list()]
    return subject_list + student_list


def collect_score(student:int, subject:int)->int:
    score = input(f'''
Entering score for student {student}
Enter score for subject {subject}
''')
    while not bool(re.match(r'^(?:100|[1-9]?[0-9])$', score)):
        print('Invalid score')
        print('Score must a number between 0 to 100')
        score = input(f'''
Entering score for student {student}
Enter score for subject {subject}
''')
    print_saved_successfully()
    return int(score)


def fill_list()->list:
    merged = merge_list()
    for student in range(1,len(merged)):
        for subject in range(1,len(merged[0])-3):
            merged[student].append(collect_score(student,subject))
    return merged

def fill_total_and_average()->list:
    sum_score = 0
    size = 0
    lst = fill_list()
    for student in range(1,len(lst)):
        for subject in range(1,len(lst[0])-3):
            sum_score += lst[student][subject]
            size += 1
        lst[student].append(sum_score)
        formatted_result = "{:.2f}".format((sum_score/size))
        lst[student].append(formatted_result)
        sum_score = 0
        size = 0
    return lst


def fill_position()->list:
    lst = fill_total_and_average()
    total = []
    for grades in range(1,len(lst)):
        total.append(lst[grades][len(lst[0])-3])
    total.sort(reverse=True)
    for element in total:
        for grades in range(1, len(lst)):
            if element == lst[grades][len(lst[0])-3]:
                lst[grades].append((total.index(element))+1)
    return lst

def subject_summary(table_list:list):
    highest_scoring_student = 0
    lowest_scoring_student = 101
    total_score = 0
    average = 0
    passes = 0
    fails = 0
    highest_student = ''
    lowest_student = ''
    for grades in range(1,len(table_list[0])-3):
        for grade in range(1,len(table_list)):
            total_score += table_list[grade][grades]
            if table_list[grade][grades] < 50: fails += 1
            else: passes += 1
            if table_list[grade][grades] > highest_scoring_student:
                highest_scoring_student = table_list[grade][grades]
                highest_student = f'student {grade}'
            if table_list[grade][grades] < lowest_scoring_student:
                lowest_scoring_student = table_list[grade][grades]
                lowest_student = f'student {grade}'
            average += 1
        print(f'''
Subject{grades}
Highest Scoring student is: {highest_student} scoring {highest_scoring_student}
Lowest scoring student is: {lowest_student} scoring {lowest_scoring_student}
Total score is: {total_score}
Average score is: {(total_score/average):.2f}
Number of passes: {passes}
Number of fails: {fails}
''')
        highest_scoring_student = 0
        lowest_scoring_student = 101
        total_score = 0
        average = 0
        passes = 0
        fails = 0

table = fill_position()
for elements in range(len(table)):
    if elements == 0:
        print('=' * (len(table[0]) * 15))
    for element in table[elements]:
        if elements == 0:
            print(f'{element:>10}', end='\t')
            continue
        print(f'{element:>10}',end='\t')
    print()
    if elements == 0:
        print('=' * (len(table[0]) * 15))
    if elements == (len(table)-1):
        print('=' * (len(table[0]) * 15))
        print('=' * (len(table[0]) * 15))
subject_summary(table)









