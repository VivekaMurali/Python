try:
  a=int(input('Enter a integer:'))
  if a<90 or a>120:
    raise ValueError('Abnormal condition')
except ValueError as ve:
  print(ve)
else:
  print(a,'is within 90 and 120')
