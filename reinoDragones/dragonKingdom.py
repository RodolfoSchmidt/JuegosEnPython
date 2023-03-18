import random
import time


def displayIntro():
    print('Estas en una tierra llena de dragones. Frente a ti')
    print('hay dos cuevas. En una de ellas, el dragon es generoso')
    print('y amigable y compartira su tesoro contigo. El otro dragon')
    print('es codicioso y hambriento, y te va a comer de un bocado.')
    print()


def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('A que cueva quieres entrar? 1 o 2?')
        cave = input()
    return cave


def caveExploration(caveNumber):
    print('Te aproximas a la cueva...')
    time.sleep(2)
    print('Es oscura y espeluznante...')
    time.sleep(2)
    print('Un gran dragon aparece súbitamente frente a ti! Abre sus fauces y...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if caveNumber == str(friendlyCave):
        print('Te regala su tesoro!')
    else:
        print('Te engulle de un bocado!')


playAgain = 'si'
while playAgain == 'si' or playAgain == 's':
    displayIntro()
    caveNumber = chooseCave()
    caveExploration(caveNumber)

    print('Quieres jugar de nuevo? (si o no)')
    playAgain = input()
