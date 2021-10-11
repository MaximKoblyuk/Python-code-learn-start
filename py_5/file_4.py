# num=int(input('Введите число :'))
# num2=0
# while num !=0:
#   num=int(input('Введите еще :'))
#   if num % 2 == 0 and num != 0:
#     num2 += 1
#   elif num == 0:
#     break
# print(num2)

count=0
arr=list()
for i in range(0,1000):
  num=int(input('Введите число :'))
  if num==0:
    break
  arr.append(num)

for n in arr:
  if n % 2 == 0:
    count += 1

print(count)
