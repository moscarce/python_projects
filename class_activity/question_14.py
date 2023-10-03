def check_letter(letter:str):
    letter = letter.upper()
    return f'Letter {letter} is vowel' if letter in 'AEIOU' else f'Letter {letter} is not vowel'


print(check_letter('s'))
