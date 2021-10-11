profit=int(input('Введите суму: '))
if profit >= 0:
  if profit <= 10000:
    tax=profit * 13 / 100
  elif profit <= 50000 :
    tax= ((profit - 10000) * 20 / 100) + (10000 * 13 / 100)
  else:
    tax=((profit- 50000)* 30 / 100)+(40000 * 20 / 100) + (10000 * 13 / 100)
  if tax > 0 :
    print('Размер налога ',tax)
else:
  print('Ошибка: доход не может быть отрицательным')