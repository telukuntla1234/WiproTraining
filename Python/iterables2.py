Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> dict1 = {1:10,2:20,3:30}
>>> dict1
{1: 10, 2: 20, 3: 30}
>>> dict1[2]
20
>>> dict2 = {'a':10, 'b':20,'c':30}
>>> dict2
{'a': 10, 'b': 20, 'c': 30}
>>> dict2['c']
30
>>> stud = {'rno':101, 'name':'sindhu', 'city': 'hydetabad'}
>>> stud
{'rno': 101, 'name': 'sindhu', 'city': 'hydetabad'}
>>> stud['name'] = 'telu'
>>> stud
{'rno': 101, 'name': 'telu', 'city': 'hydetabad'}
>>> stud['fname'] = 'srinu'
>>> stud
{'rno': 101, 'name': 'telu', 'city': 'hydetabad', 'fname': 'srinu'}
>>> stud.get('name')
'telu'
>>> stud.keys()
dict_keys(['rno', 'name', 'city', 'fname'])
>>> stud.values()
dict_values([101, 'telu', 'hydetabad', 'srinu'])
>>> stud.pop('fname')
'srinu'
>>> stud
{'rno': 101, 'name': 'telu', 'city': 'hydetabad'}
