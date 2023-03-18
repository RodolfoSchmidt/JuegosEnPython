La entrada es escrita por el usuario desde el teclado e introducida a la computadora. La salida es el texto
mostrado en la pantalla. En Python, la función print() se puede usar para mostrar salidas de
texto en la pantalla. Pero hay más para aprender sobre cómo funcionan las cadenas y el print()
en Python.
Las líneas de la 1 a la 4 tienen tres llamadas a la función print(). No quieres que el jugador lea
de inmediato el remate del chiste, así que hay una llamada a la función print() después del
primer print(). El jugador puede leer la primera línea, presionar INTRO, y entonces leer el
remate del chiste.
El usuario todavía puede escribir una cadena y pulsar INTRO, pero esta cadena devuelta no está
siendo almacenada en ninguna variable. El programa tan solo lo olvidará y se moverá a la
siguiente línea de código.
La última llamada a la función print() no tiene argumento de cadena. Esto le indica al programa
que solamente escriba una línea en blanco. Las líneas en blanco pueden ser útiles para evitar que
el texto quede unido.
Caracteres de Escape 5. print('¿Porqué vuelan los pájaros pa\'l sur?') 6. input() 7. print('¡Porque caminando tardarían muchísimo!') 8. print()
En el primer print() de arriba, ha una barra invertida justo antes de la comillas simple (esto es,
el apóstrofo). Nota que \ es una barra inversa, y / es una barra inclinada. Esta barra inversa
indica que la letra que está a su derecha es una caracter de escape. Un caracter de escape te
permite imprimir caracteres que son difíciles de introducir en el código fuente. En esta llamada a
print() el caracter de escape es una comilla simple.
El caracter de escape comilla simple está allí porque de otra manera Python pensaría que la
comilla indica el final de la cadena. Pero esta comilla necesita formar parte de la cadena. La
comilla simple de escape le indica a Python que la comilla simple es literalmente una parte de la
cadena en lugar de indicar el final del valor de la cadena.
Algunos Otros Caracteres de Escape
¿Qué pasa si realmente quisieras escribir una barra invertida?. Esta línea de código no
funcionaría:

> > > print('Él se fue volando en un helicóptero verde\turquesa.')
> > > Él se fue volando en un helicóptero verde urquesa.
> > > Esto es porque la "t" en "turquesa" fue vista como un caracter de escape debido a que estaba
> > > después de una barra inversa. El caracter de escape t simula la pulsación de la tecla TAB de tu
> > > teclado. Hay caracteres de escape para que las cadenas puedan tener caracteres que no se pueden
> > > escribir.
> > > En lugar de eso, prueba con esta línea:
> > > print('Él se fue volando en un helicóptero verde\\turquesa.')
> > > Él se fue volando en un helicóptero verde\turquesa.

Caracter de Escape Lo Que Imprime
\\ Barra inversa (\)
\' Comilla simple (')
\" Comilla doble (")
\n Salto de línea
\t Tabulador

Comillas Simples y Dobles
La cadenas en Python no tienen que estar siempre entre comillas simples. También puedes
ponerlas entre comilas dobles. Estas dos líneas imprimen lo mismo:

> > > print('Hola mundo')
> > > Hola mundo
> > > print("Hola mundo")
> > > Hola mundo
> > > Pero no puedes mexzclar las comillas. Esta línea devolverá un error si intentas utilizarla:
> > > print('Hola mundo")
> > > SyntaxError: EOL while scanning single-quoted string

El Argumento de Palabra end 9. print('¿En qué se parecen una familia, un bombero y un barco?') 10. input() 11. print("No sé... ¿en qué se parecen?") 12. input() 13. print('En que el bombero y el barco tienen casco.') 14. input() 15. print('¿Y la familia?', end='') 16. print(' -Bien, gracias.')
¿Te diste cuenta del segundo parámetro en el print de la línea 15?. Normalmente, print() añade
un salto de línea al final de la cadena que imprime. Por esta razón, una función print() en
blanco tan solo imprimirá una nueva línea. Pero la función print() tiene la opción de un
segundo parámetro (que tiene nombre “end” (fin)).
La cadena en blanco dada se llama argumento de palabra clave. El parámetro final tiene un
nombre específico, y para pasar un argumento a ese parámetro en particular necesitamos utilizar
la sintáxis end=.
Pasando una cadena en blanco usando end, la función print() no añadirá un salto de linea al
final de la cadena, en lugar de esto añadirá una cadena en blanco. Por esta razón ' -Bien,
gracias.' aparece junto a la línea anterior, en lugar de sobre una nueva línea. No hubo salto de
línea después de la cadena '¿Y la familia?'.
