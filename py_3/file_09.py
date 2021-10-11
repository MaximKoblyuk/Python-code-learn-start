tach=int(input('Введите значения циферблата   ' )) 
day=int(input('Введите дату '))
a=tach//100
#print(a)
b=tach%100//10
#print(b)
c=tach%10
#print(c)
if (a+b+c) > day :
  print('Сброс')
  print('0 km')
else:
  print('Сегодня не сломался')
  print( tach,'km')