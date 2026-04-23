'''
#list
numbers = [11,22,98,54,63,45,20,45]

for number in numbers:
    print(number%10, end = '\t')

#tuple
numbers = (11,22,566,45,34,54,55)

for number in numbers:
    print(number%10, end = '\t')

#set
numbers = {11, 22, 98, 54, 63, 45, 20, 45}

for number in numbers:
    print(number % 10, end='\t')'''

stud = {'rno' : 101, 'name' : 'sindhu', 'city':'hyd'}

for k,v in stud.items():
    print(k, '--', v)
