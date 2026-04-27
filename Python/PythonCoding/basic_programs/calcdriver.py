from basic_programs.calc import Calc

calcobj = Calc()
print(calcobj.add(a=10 , b =5))
print(calcobj.sub(a=10 , b =5))
print(calcobj.mul(a=10 , b =5))

numbers = [10, 30, 40]
count = len(numbers)
print(f'length : {count}')
000
try:
    res = calcobj.fdiv(a=10, b=5)
    for i in range(0, count+1):
        print(numbers[i])
except IndexError:
    print('list index out of range')
except ZeroDivisionError:
    print('0 in denominator')
except:
    print('oopsss...')
else:
    print(res)
finally:
    print('Done')









