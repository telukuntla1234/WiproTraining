
import re

# txt =input('Enter a text :') #India is my country
# bpat = input('Enter beginning pattern :') #India
# epat = input('Enter ending pattern :') #country
# bpat = '^' + bpat #^India
# epat = epat + '$' #try$
#
# if re.search(pattern=bpat, string=txt):
#     print('Beginning pattern available')
# else:
#     print('Beginning pattern not available')
#
# if re.search(pattern=epat, string=txt):
#     print('ending pattern available')
# else:
#     print('ending pattern not available')

#digit
# mbno = input('Enter a text :')
# pat = r"\d"
#
# if re.fullmatch(pattern=pat, string=mbno):
#     print('only digits')
# else:
#     print('other chars available')


#username
# un = input('Enter Un :')
# pat = r"^[a -z_]{8,}$"
#
# if re.match(pattern=pat, string=un):
#     print('valid')
# else:
#     print('invalid')

#email

# '''emailadd = input('Email : ')
# pat = r"^[a-zA-Z0-9_]+@[a-z]+\.[a-z]+$"
#
# if re.match(pattern=pat, string=emailadd):
#     print('valid')
# else:
#     print('invalid')'''

#password
# pwdtxt = input('pwd :')
# pat = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@_-]).{8,}$"
#
# if re.match(pattern=pat, string=pwdtxt):
#     print('valid')
# else:
#     print('invalid')


txt = input('text : ')
pat=r"\s+"

# print(re.sub(pattern=pat, string=txt,repl=' '))

print(re.split(pattern=pat, string=txt))
