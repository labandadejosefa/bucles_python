# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''

print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio

operacion = None

while operacion != 'FIN':
    num1 = float(input('Ingrese un número cualquiera:\n'))
    num2 = float(input('Ingrese otro número cualquiera:\n'))
    operacion = str(input('Para los números ingresados, escoja una operación a realizar:\n"+" suma\n"-" resta\n"*" producto\n"/" cociente\n"**" potenciación\n"FIN" salir del programa\n'))
    if operacion == '+':
        suma = num1 + num2
        print(f'La SUMA de {num1} y {num2}, es {suma}')
    elif operacion == '-':
        resta = num1 - num2
        print(f'La RESTA de {num1} menos {num2}, es {resta}')
    elif operacion == '*':
        producto = num1*num2
        print(f'El PRODUCTO de {num1} y {num2}, es {producto}')
    elif operacion == '/':
        if num2 ==0:
            print('La operación no está definida')
        else:
            cociente = num1 / num2
            print(f'El COCIENTE entre {num1} y {num2}, es {round(cociente,2)}')
    elif operacion == '**':
        if (num1 ==0 and num2 ==0) or (num1 == 0 and num2 < 0):
            print('La operación no está definida')
        else: 
            potencia = pow(num1, num2)
            print(f'La POTENCIA de base {num1} y exponente {num2}, es {potencia}') 
    else:
        print('Escogió la opción de finalizar la ejecución')
        break

    
        
        
    
        
        
