# Juego de adivina el número!

import random

intentosRealizados = 0

print('¡Hola! ¿Cómo te llamas?')
nombreUsuario = input()

numero = random.randint(1, 20)

print('Bueno, ' + nombreUsuario +
      ', estoy pensando en un número entre el 1 y el 20.')

while intentosRealizados < 5:
    print('Intenta adivinar en 5 intentos:')
estimacion = input()
estimacion = int(estimacion)

intentosRealizados = intentosRealizados + 1

if estimacion < numero:
    print('Tu estimación es baja')
if estimacion > numero:
    print('Tu estimación es alta.')

if estimacion == numero:
    intentosRealizados = str(intentosRealizados)
    print('¡Bien hecho ' + nombreUsuario +
          '! Has adivinado mi número en ' + intentosRealizados + ' intentos')
if estimacion != numero:
    numero = str(numero)
    print('Has perdido. el número en que estaba pensando era: ' + numero)
