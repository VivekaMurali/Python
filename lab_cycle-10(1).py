

try:
  a=int(input('Enter number1:'))
  b=int(input('Enter number2:'))
  print("{0}/{1}={2}".format(a,b,a/b))
except ValueError as ve:
  print("Value error:",ve)
except (ZeroDivisionError,ValueError) as e:
  print(e)
else:
  print('Division successful')
finally:
  print(' Program executed')
