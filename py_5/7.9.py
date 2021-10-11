orderliness = True
maxx = 0
for number in range(1,10+1):
  number1 = int(input('Введите число: '))
  if maxx < number1:
    maxx = number1
  else: 
    orderliness = False
if orderliness == True:
  print('Числа упорядочены!')
else:
  print('Числа не упорядочены!') 