number = int(input('Введите число: '))
while number <= 0:
 summ = int(input('Введите число: '))
 summ += number
 print(summ)

password=int(input('Введите пароль: '))
while password != 235 :
  print('Неверный пароль!')
  password=int(input('Попробуйте ещё раз: '))
print('Пароль верный! Добро пожаловать.')


money=int(input('Сколько отложить денег? '))
while money <= 500000 :
  summ=int(input('Сколько отложить денег? '))
  money += summ 
  print('Еще накопи ')
print('Ура!')


weather =int(input('Сколько сейчас градусов: '))
metrs = 0
while weather > 15 :
  metrs += 20 
  weather -= 2 
  if weather <= 15 :
    break 
  metrs += 10 
print('Пройдено метров', metrs)
  


nummber =int(input('Введите число : '))
summ = 0
while nummber != 0 :
  last_num = nummber % 10
  print( last_num )
  if last_num == 5 :
    print('Обнаружена ошибка ')
    break
  summ += last_num 
  print ('Сумма ' , summ)


count= int(input('Ведите время : '))
while count <= 10 :
 if count == 0:
   print('Время вышло!')
   break
 else:
   count -= 1
   print(count)


rate_check = False 
while True :
  active= int(input('Продолжаем работать 1/0  :'))
  if active == 0 :
    print ('Приложение закрывается…')
    break
  rate= int(input('Поставте оценку  1/0  :'))
  if rate == 1 :
    rate_check = True 
print ('Работа завершина ')
if rate_check == True :
  print('Пользиватель поставил оценку')



password=input('Введите пароль: ')
if password == "0550" :
  print ('Код верный, завершаю работу...')
  print ('Спасибо за скейт ')
else:
  while password != "0550" :
    print('Компьютер заблокирован. Вернёшь скейт — скажу код разблокировки!')
    password=input('Введите код : ')


print('Пароль верный! Добро пожаловать.')