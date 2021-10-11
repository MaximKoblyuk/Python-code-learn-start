print ('Начался 8-часовой рабочий день')
hour= 0 
work_all= 0 
shop=0
while hour < 8 :
  hour +=1 
  print(hour, 'час' )
  work=int(input('Сколько задач решит Максим?'))
  call=int(input('Звонит жена. Взять трубку?'))
  work_all += work
  if call == 1 :
    shop=1
    #print ('Нужно зайти в магазин')
    work_all += call
  if hour >= 8:
    print('Рабочий день закончился. Всего выполнено задач: ', work_all)
if shop==1:
  print ('Нужно зайти в магазин')
