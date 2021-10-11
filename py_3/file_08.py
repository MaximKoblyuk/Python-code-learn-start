hour=int(input('Сколько часов? : '))
kredit=int(input('Введите остаток по кредиту :'))
food=int(input('Введите траты на еду :'))
summa=(200*hour)/(2**3)+hour
if (kredit+food) > summa :
 print('Часов не хватает. Придётся поработать!') 
else :
  print('Часов хватает. Можно отдохнуть')
