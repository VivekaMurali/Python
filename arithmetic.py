from arithmetic.add import add 
from arithmetic import sub as s
from arithmetic.carithmetic.mul import *
from arithmetic.carithmetic.div import *
a=int(input('Enter num1.:'))
b=int(input('Enter num2:'))
print('Sum=',add(a,b))
print('Subtraction=',s.Sub(a,b))
print('Mulplication=',mul(a,b))
print('Division=',div(a,b))
