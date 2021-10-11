num=int(input('Print number: '))
a=num % 10
b=num % 100 // 10
c=num // 100 % 10
d=num // 1000
rec_number=a * 1000 + b * 100 + c * 10 + d
print('Revers number: ',rec_number)