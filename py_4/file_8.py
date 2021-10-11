m_2=int(input('Введите м2 :'))
price= int(input('Введите цену : '))
if m_2 >= 100 and price <= 1000000 :
  print ('Квартира подходит ')
elif m_2 >= 80 and price <= 7000000 :
  print ('Квартира подходит но будет по меньше ')
else:
  print ('Вариант не подходит')