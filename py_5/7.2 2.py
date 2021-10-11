winers = 0
for ticket in 345, 19, 87, 1020, 421:
  if ticket % 5 == 0 :
    print( ticket, 'Win')
    winers += 1
print ('How many',winers)
