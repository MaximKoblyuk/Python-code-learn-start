x=int(input('Введите икс: '))
y=int(input('Введите игрек :'))
if x<y :
  print('X меньше Y')
if x>y :
  print('X больше Y')
if x == y :
  print('X равен Y')



  bank=int(input('Сколько денег на счету? '))
if bank > 75000:
 bank -= 75000 
 print('Курс успешно приобретён')
 if bank < 5000:
   bank += 1000
   print('Сделана скидка')
else:
  print('Не хватает денег на счету ')
print('Остаток на счету :', bank)
print('Хорошего дня!')


many=int(input('Сколько денег дала мать ? :'))
if many >= 60 :
  many -= 60
  print('На сыр денег хватает ')
  if many >= 20 :
   print('И на мороженое тоже!')
  else :
   print('Денег маловато')


income=int(input('Введите суму '))
income >= 0
while True:
    if income < 10000:
        tax = 0
        print('LOW TAX')
    elif income > 10000 and income <= 30000:
        tax = (income-10000)*(0.1)
        print(tax)
    elif income > 30000 and income <= 70000:
        tax = (income-30000)*(0.2) + 2000
        print(tax)
    elif income > 70000:
        tax = (income - 70000)*(0.3) + 10000
        print(tax)



profit=int(input('Введите суму: '))
if profit >= 0:
  if profit < 10000:
    tax=profit * 13 / 100
    print('Размер налога 13% ',tax)
  elif profit < 50000 :
    tax=profit * 20 / 100
    print('Размер налога 20% ',tax)
  else:
    tax=profit * 30 / 100
    print('Размер налога 30% ',tax)
else:
  print('Ошибка: доход не может быть отрицательным')
   


a=int(input('Введите вес монеты 1:'))
b=int(input('Введите вес монеты 2:'))
c=int(input('Введите вес монеты 3:'))
if a > b :
  print('Монета 2 легче')
elif a >c :
  print('Монета 3 легче')
if b > a :
  print('Монета 1 легче')
if b > c :
  print('Монета 3 легче')
if c > a :
  print('Монета 1 легче') 
if c > b :
  print('Монета 2 легче') 


year=int(input('Введите год :'))
speed=int(input('Введите количество скоростей: '))
if year >= 2018 and speed >= 24 :
  print ('Нам подходит ')
else:
  print('Не подходит')



point=int(input('Сколько баллов набрал? :'))
gold=int(input('Есть медаль?: '))
if point >= 280 and gold >= 1:
  print('Поздравляем! Ты поступил!')
else:
  print('К сожалению, ты не прошёл в наш университет.')


x=int(input('Введите температуру :'))
low_temp = int(input('Введите нижный порог температутри :'))
hi_temp = int(input('Введите верхный порог температури :'))
if low_temp < 0 or hi_temp >= 100 :
  print ('Опасность темперптур ')
elif x < 0 or x > 100 :
  print ('Опасность темперптур ')
else:
  print('Все нормально !')
  