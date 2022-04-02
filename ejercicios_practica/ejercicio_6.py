# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicio de secuencias numéricas

# Pedir por consola dos números que representen el principio y fin de una
# secuencia numérica.
# Realizar un bucle "for" que recorra esa secuencia armada con "range"
# y cuante cuantes números son negativos y cuantos números son mayor o igual a cero
# Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
# sino que va hasta el anterior

inicio = int(input('Ingrese el primer número de la secuencia\n'))
fin = int(input('Ingrese el último número de la secuencia\n'))

cantidad_numeros_positivos = 0  # Inicializo el contador en 0

cantidad_numeros_negativos = 0 # agrego otro contador para negativos

# for ... in range(....)

for k in range(min(inicio, fin), max(inicio, fin)+1):
    if k < 0:
        cantidad_numeros_negativos += 1
    else:
        cantidad_numeros_positivos +=1

# Imprimir el valor de la cantidad de números positivos y negativos
print(f'La cantidad de números negativos entre {min(inicio, fin)} y {max(inicio, fin)}, es {cantidad_numeros_negativos}.\nLa cantidad de números mayores o iguales que cero en el mismo intervalo, es {cantidad_numeros_positivos}.')
print("terminamos!")
