# create a list with 5 fruits
from traceback import print_tb

fruits = ['apple','mango','banana','grpaes','pineapple']
print('Initial list : ' ,fruits)

#Add two fruits and remove one
fruits.append('orange')
fruits.append('kiwi')
fruits.remove('banana')
print('Updated list : ',fruits)

#Access second and fourth fruits
print("Second fruit : ", fruits[1])
print('fourth fruit : ', fruits[3])

#Slice first three fruits
print('First three fruits : ', fruits[:3])

#length of the list
print('length of list : ', len(fruits))