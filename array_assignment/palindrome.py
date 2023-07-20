def palindrome(string: str):
    string =''.join(string.split())
    if string[::] == string[::-1]:
        print(f"{string} is a palindrome")
    else:
        print(f"{string} is not a palindrome")


palindrome('madam')
palindrome('deed')
palindrome('civic')
palindrome('chisom')
