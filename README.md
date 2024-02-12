El primer ejercicio verifica la longitud de una palabra ingresada por el usuario y muestra un mensaje dependiendo de la cantidad de letras en la palabra.

Primero, se solicita al usuario que ingrese una palabra utilizando la función `input()` y se guarda en la variable `word`.

Luego, se realizan tres comprobaciones utilizando la función `len()` para obtener la longitud de la palabra:
  1. Si la longitud de la palabra es mayor que 8, se imprime un mensaje indicando que hay letras de sobra y se muestra la cantidad de letras en la palabra utilizando `len(word)`.
  2. Si la longitud de la palabra es menor que 4, se imprime un mensaje indicando que faltan letras y se muestra la cantidad de letras en la palabra utilizando `len(word)`.
  3. Si la longitud de la palabra está entre 4 y 8, se imprime un mensaje indicando que la palabra es correcta y que se encuentra dentro del rango.

En resumen, el código verifica la longitud de una palabra ingresada por el usuario y muestra un mensaje dependiendo de si la longitud es mayor que 8, menor que 4 o está entre 4 y 8.


El segundo ejercicio toma dos entradas del usuario, `axis_x` y `axis_y`, que representan las coordenadas de un punto en un plano bidimensional.

El código luego determina y muestra en qué cuadrante del plano se encuentra el punto, o si está en uno de los ejes o en el origen.

  - Si `axis_x > 0` y `axis_y > 0`, el punto se encuentra en el primer cuadrante.
  - Si `axis_x < 0` y `axis_y > 0`, el punto se encuentra en el segundo cuadrante.
  - Si `axis_x < 0` y `axis_y < 0`, el punto se encuentra en el tercer cuadrante.
  - Si `axis_x > 0` y `axis_y < 0`, el punto se encuentra en el cuarto cuadrante.
  - Si `axis_x != 0` y `axis_y == 0`, el punto está en el eje x.
  - Si `axis_x == 0` y `axis_y != 0`, el punto está en el eje y.
  - Si `axis_x == 0` y `axis_y == 0`, el punto está en el origen.
  - Si ninguna de las condiciones anteriores se cumple, el programa imprimirá que el punto no está en ningún cuadrante.

CONCLUSION:

  Considero personalmente que no fueron ejercicios tan complejos; sin embargo, era necesario tener claras ciertas estructuras y métodos para llegar al resultado esperado.
