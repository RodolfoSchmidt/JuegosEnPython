import random
print('Se lanzará una moneda 1000 veces, adivina cuantas veces caerá cara y cuantas cruz (Presiona Enter para comenzar)')
prediccion = input('Cuantas veces crees que caerá cara?: ')
lanzamientos = 0
caras = 0
cruz = 0
while lanzamientos < 1000:
    if random.randint(0, 1) == 1:
        caras = caras + 1
    if random.randint(0, 1) == 0:
        cruz = cruz + 1
    lanzamientos = lanzamientos + 1

print('Cruz salió ' + str(cruz) + ' veces.')
print('Cara salió ' + str(caras) +
      ' veces. ' 'Tu dijiste: ' + prediccion + ' veces.')
print('¿Acertaste?')
