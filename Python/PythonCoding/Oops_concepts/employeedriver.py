#driver
from Oops_concepts.employeedetails import EmployeeDetails

eno = int(input('Enter employee no :'))
name = input('emp name :')
bp = float(input('basic pay :'))

employee = EmployeeDetails(empno = eno , ename = name, basicpay = bp)

print('Emp no : ', employee.empno)
print('Emp name :', employee.ename)
print('Basic pay : ', employee.basic_pay)
print('Salary : ', employee.calculate_netsal())


