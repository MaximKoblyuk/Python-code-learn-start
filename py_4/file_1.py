point=int(input('Введите количество опыта: '))
if point <= 1000  :
  print ('У Вас 1 уровень')
elif point < 2500 :
  print ('У Вас 2 уровень')
elif point < 5000 :
  print ('У Вас 3 уровень')
else:
  print('У Вас 4 уровень')



  #ввариант 2

  point=int(input('Введите количество опыта: '))
if point <= 1000  :
  print ('У Вас 1 уровень')
elif point in range(1001,2501):
  print ('У Вас 2 уровень')
elif point in range(2501,5001) :
  print ('У Вас 3 уровень')
else:
  print('У Вас 4 уровень')