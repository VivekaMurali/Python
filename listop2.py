from listop import *
a=input('Enter list:')
l=a.split(' ')
l=[int(i) for i in l]
print('Unique List=',Unique(l))
print('Square of list:',Square(l))
