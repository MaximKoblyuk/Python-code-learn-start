totalcards=int(input('Сколько карточек?'))
totalsum= 0
lostSum= 0
for card in range(1,totalcards + 1):
  totalsum += card
for card in range (totalcards - 1):
 lost_card=int(input('Какая карточка пропала?'))
 totalsum -= lost_card
print ('Номер карточкы',totalsum)



#totalsum=(1+totalcards) / 2 * totalcards