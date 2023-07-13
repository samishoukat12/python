guessNum=int(input('Enter Number to guess: '))
import random

def guessGame(guessNum):
   randomNum=random.random(1,9)
   if guessNum==randomNum:
      print('your guess is right')
   else:
      print('tou guess it wrong')

guessGame(guessNum)
