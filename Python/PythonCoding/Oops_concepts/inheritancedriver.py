from Oops_concepts.college import College
from Oops_concepts.student import Student

cc = int(input('C code : '))
cn = input('C name : ')
ci = input('C city : ')
rno = int(input('Roll no : '))
sn = input('Enter student name :')
m1 = int(input('M1 :'))
m2 = int(input('M2 :'))
m3 = int(input('M3 : '))

# project = College(ccode= cc, cname=cn, ccity=ci)

project = Student(ccode=cc, cname=cn, ccity=ci, rno=rno, sname=sn,
                  m1=m1, m2=m2, m3=m3)

project.welcome_message()
project.display_college_details()
print(f'Roll No : {project.rollno} \n Name : {project.stuname} \n'
      f'Total : {project.calculate_total()} \nAverage : {project.calculate_average()}')




