
kostia=int(input('Кубик Кости : '))
owner=int(input('Кубик Владельца: '))
if (owner-kostia) >= 0:
  print('kostya owes USD: ', (owner-kostia)*1000)
elif (kostia-owner)==0:
  print('noting')
else:
  print('owner owes USD: ', (kostia+owner)*1000)
print('Game over')
