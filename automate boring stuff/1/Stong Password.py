import re

password = input('Enter the password:')
passwordRegex1 = re.compile(r'[a-z]')
passwordRegex2 = re.compile(r'[A-Z]')
passwordRegex3 = re.compile(r'[0-9]')
passwordLenRegex = re.compile(r'(\S{8})+')
if not (passwordLenRegex.search(password) and passwordRegex1.search(password) and passwordRegex2.search(password) and passwordRegex3.search(password)):
    print('Spaces are not allowed & Password should be atleast 8 char')


print('your password is strong')
