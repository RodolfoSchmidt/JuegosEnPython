#Adivina el Número

##Descripción

El programa genera un número aleatorio entre 1 y 20, y el usuario debe adivinarlo en 5 intentos. El programa le da pistas al usuario para que pueda adivinar el número tras fallar en un intento.

##VEAMOS EL CÓDIGO:

```import random

intentosRealizados = 0

print('¡Hola! ¿Cómo te llamas?')
nombreUsuario = input()

numero = random.randint(1, 20)

print('Bueno, '+ nombreUsuario +', estoy pensando en un número entre el 1 y el 20.')

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
        break
if estimacion == numero:
    intentosRealizados = str(intentosRealizados)
    print('¡Bien hecho '+ nombreUsuario +'! Has adivinado mi número en ' + intentosRealizados + ' intentos')
if estimacion != numero:
    numero = str(numero)
    print('Has perdido. el número en que estaba pensando era: '+ numero)
```

en principio vemos un import. import es una sentencia que nos permite importar módulos. En este caso importamos el módulo random. El módulo random nos permite generar números aleatorios.
en este caso llamandolo con random.randint(1,20) generamos un número aleatorio entre 1 y 20.

Después vemos la variable intentosRealizados. Esta variable nos servirá para llevar la cuenta de los intentos que lleva el usuario. La inicializamos a 0.

tenemos un bucle dentro de nuestro programa.
`while intentosRealizados < 5:`
Este bucle se ejecutará mientras que el número de intentos realizados sea menor que 5. En este caso, el bucle se ejecutará 5 veces.
para entender los bucles, tenemos que hablar de los bloques, Un bloque comienza cuando la indentación de una línea se incrementa (usualmente en cuatro espacios). Cualquier línea subsiguiente que también esté indentada por cuatro espacios es parte del bloque. El bloque termina cuando hay una línea de código con la misma indentación que antes
de empezar el bloque. Esto significa que pueden existir bloques dentro de otros bloques.

Otro dato a tener el cuentas es el tipo de DATO BOOLEANO El tipo de datos Booleano tiene sólo dos valores: True (Verdadero) o False (Falso). Estos valores deben escribirse con “T” y “F” mayúsculas. El resto del nombre del valor debe estar en minúscula. Usarás valores Booleanos (llamados bools por brevedad) con operadores de
comparación para formar condiciones. (Las condiciones serán explicadas más adelante.)

En el código también tenemos los operadores de comparación.
`if estimacion < numero:`
La expresión que sigue a la palabra reservada while (la parte intentosRealizados < 6)
contiene dos valores (el valor en la variable intentosRealizados, y el valor entero 6)
conectados por un operador (el símbolo <, llamado el símbolo “menor que”). El símbolo < se
llama un operador de comparación.

Signo del Operador Nombre del Operador

```
< Menor que
> Mayor que
> <= Menor o igual a
> = Mayor o igual a
> == Igual a
> != Diferente a
```

Debemos hablar también de las CONDICIONES:
Una condición es una expresión que evalúa a True o False.
En el código también tenemos la sentencia if. La sentencia if es una de las sentencias de control de flujo más importantes en Python. La sentencia if nos permite ejecutar un bloque de código si una condición es verdadera. Si la condición es falsa, el bloque de código no se ejecuta. La sintaxis de la sentencia if es la siguiente:

```if condición:
    bloque de código
```

La Diferencia Entre = y ==
Intenta no confundir el operador asignación (=) y el operador de comparación “igual a” (==). El
signo igual (=) se usa en sentencias de asignación para almacenar un valor en una variable,
mientras que el signo igual-igual (==) se usa en expresiones para ver si dos valores son iguales. Es
fácil usar uno accidentalmente cuando quieres usar el otro.
Sólo recuerda que el operador de comparación “igual a” (==) está compuesto por dos caracteres,
igual que el operador de comparación “diferente a” (!=) que también está compuesto por dos
caracteres.

una sentencia if. La ejecución correrá el código en el siguiente bloque si la
condición de la sentencia if se evalúa a True. Si la condición es False, entonces el código en el
bloque if se omite. Mediante el uso de sentencias if, puedes hacer que el programa sólo ejecute
ciertas partes del código cuando tú quieras.
La sentencia if funciona casi igual que una sentencia while. Pero a diferencia del bloque while,
la ejecución no vuelve atrás hasta la sentencia if cuando termina de ejecutarse el bloque if.
Simplemente continúa en la línea siguiente. En otras palabras, las sentencias if no generan un
bucle. Mira la Figura 4-3 para ver una comparación de las dos sentencias.

Abandonando los Bucles Anticipadamente con la sentencia break

La sentencia if en la línea 25 comprueba si la estimación es igual al entero aleatorio. Si lo es, el
programa ejecuta la sentencia break de la línea 26.
Una sentencia break indica a la ejecución que salga inmediatamente del bucle while y se mueva
a la primera línea a continuación del mismo. (Las sentencias break no se molestan en volver a
revisar la condición del bucle while, sólo salen del bucle instantaneamente.)
La sentencia break es simplemente la palabra reservada break en sí misma, sin condición o dos
puntos.
Si el jugador adivinó el número no es igual al número entero aleatorio, la ejecución alcanza la
parte inferior del bloque while. Esto significa se repetirá la ejecución de nuevo a la parte superior
y vuelva a comprobar el estado de la línea 12 (intentosRealizados < 6). Recuerdo que
después de los intentosRealizados = intentosRealizados + 1 línea de código se ejecuta, el
nuevo valor de intentosRealizados es 1. Porque 1 <6 es cierto que la ejecución entra en el
bucle de nuevo.
Si el jugador continúa realizando intentos demasiado altos o bajos, el valor de
intentosRealizados cambiará a 2, luego 3, luego 4, luego 5, luego 6. Cuando
intentosRealizados tiene almacenado el número 6, la condición de la sentencia while es False,
dado que 6 no es menor que 6. Como la condición de la sentencia while es False, la ejecución se
mueve a la primera línea después del bloque while, línea 28.
