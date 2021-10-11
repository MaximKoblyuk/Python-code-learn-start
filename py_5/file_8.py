num_x=int(input('Вклад в банке :'))
num_p=int (input('Увеличивается на сколько процентов :'))
num_y=int(input('Конечная сумма :'))
time= 0

while num_x < num_y :
  num_x=(num_x*(1+num_p/100))//1
  time=time+1

print('Через', time , 'лет вклад составит ' , num_y)