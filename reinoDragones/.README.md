En este juego aplicaremos las funciones.

En el juego, el jugador esta en una tierra llena de dragones. Todos los dragones viven en cuevas junto a sus grandes montones de tesoros. Algunos dragones son amigables y compartirán su tesoro contigo. Otros dragones son codiciosos y hambrientos, y te comerán inmediatamente. El jugador se encuentra frente a dos cuevas, una con un dragón amigable y otra con un dragón hambriento.

bien al observar el código. vemos lo siguiente. primero que importamos dos modulos. uno random y otro time. y una funcion con la sentencia def. la sentencia def crea, es decir, una nueva funcion que puede ser llamada mas adelante en el programa.

las partes de una sentencia def. comienza con la palabra reservada def. seguida por un nombre de funcion con poarentesis. y dentro de los parentesis, los parametros de la funcion. y finalmente, un dos puntos.
la llamada de la funcion va luego de definir la misma.

cuando usamos en la funcion cave, con while. lo que hacemos es generar un bucle que seguira preguntando hasta que el jugador eliga una de las dos respuestas posibles.

vemos tambien en el código la utilización de operadores and y or.

Miremos otra vez la línea 13: 13. while cueva != '1' and cueva != '2':
La condición tiene dos partes conectadas por el operador Booleano and. La condición es True
sólo si ambas partes son True.
La primera vez que se comprueba la condición de la sentencia while, cueva está definida como
la cadena vacía, ''. La cadena vacía no es igual a la cadena '1', luego el lado izquierdo se evalúa
a True. La cadena vacía tampoco es igual a la cadena '2', por lo que el lado derecho se evalúa a
True.
Entonces la condición se transforma en True and True. Como ambos valores Booleanos son
True, la condición finalmente se evalúa a True. Luego la ejecución del programa entra al bloque
while.
Entorno Global y Entorno Local
Las variables de tu programa son olvidadas en cuanto el programa termina. Lo mismo ocure con
estas variables creadas mientras la ejecución está dentro de la llamada a una función. Las
variables se crean cuando la función es llamada y se olvidan cuando la función devuelve un valor.
Recuerda, las funciones son como mini-programas dentro de tu programa.
Cuando la ejecución está dentro de una función, no puedes modificar las variables fuera de la
función, incluidas variables de otras funciones. Esto es porque esas variables existen en un
“entorno” diferente. todas las variables existen en el entorno global o en el entorno local de la
llamada a una función.
El entorno exterior a todas las funciones se llama entorno global. El entorno dentro de una
función (por la duración de una llamada específica a la función) se llama entorno local.
El programa entero tiene un solo entorno global. Las variables definidas en el entorno global
puede ser leídas fuera y dentro de las funciones, pero sólo pueden ser modificadas fuera de todas
las funciones. Las variables creadas en la llamada a una función sólo pueden ser leídas o
modificadas durante esa llamada a la función.
Puedes leer el valor de las variables globales desde el entorno local, pero intentar modificar una
variable global desde el entorno local no funcionará. Lo que Python hace en ese caso es crear una
variable local con el mismo nombre que la variable global. Sería posible, por ejemplo, tener una
variable local llamada spam al mismo tienpo que existe una variable global llamada spam. Python
las considerará dos variables distintas.
Mira el siguiente ejemplo para ver qué pasa cuando intentas modificar una variable global desde
dentro de un entorno local. Los comentarios explican
