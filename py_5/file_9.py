num=7
guess=0
#guess=int(input("guess the number: "))
count=1
while guess != num:
  if guess<num:
    print("Guess again. Number should be higher.")
  elif guess > num:
    print("Guess again. Number should be lower.")
  count=+1
  guess=int(input("guess the number: "))  
print("You guessed right. Number of guesses: ", count)