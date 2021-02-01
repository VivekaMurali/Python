class MyException(Exception):pass
try:
  a=input('Enter a username:')
  b=input('Enter a password:')
  if a=='Viveka' and b=='password':
     print('Login successful')
  else:
    raise MyException('Invalid Login')
except MyException as me:
  print(me)
