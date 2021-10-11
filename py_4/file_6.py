nummer=int(input('Введите число: '))
num=abs(nummer)
if (num >= 10) and (num < 100) :
  print('All good ')
else :
  print('Not good')

# Вариант номер 2

 nummer=int(input('Введите число: '))
num=abs(nummer)
if num % 100 and num // 10  :
  print('All good ')
else :
  print('Not good')