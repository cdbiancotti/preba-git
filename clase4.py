# Escribe un programa que lea un número impar por teclado.
# Si el usuario no introduce un número impar, debe repetirse
# el proceso hasta que lo introduzca correctamente.

# numero_ingresado = 2
# while numero_ingresado % 2 == 0:
#     numero_ingresado = int(input("Ingrese un numero impar: "))
#     print('iteracion del codigo')
    

# print('Ingresaste un numero correcto!')


################################################################################
################################################################################

# Calculadora

# Escribe un programa que lea dos números por teclado y permita 
# elegir entre 4 opciones en un menú:

# 1. Mostrar una suma de los dos números  
# 2. Mostrar una resta de los dos números (el primero menos el segundo)  
# 3. Mostrar una multiplicación de los dos números  
# 4. Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará  
# 5. En caso de no introducir una opción válida, el programa informará de que no es correcta.

# num_1 = int(input('Ingrese el primer numero: '))
# num_2 = int(input('Ingrese el segundo numero: '))

# bandera = True
# while bandera:
#     opcion = input('''Ingrese operacion a ejecutar
# 1. Suma
# 2. Resta
# 3. Multiplicacion
# 4. Para salir
# opcion seleccionada: ''')
#     if opcion == '1':
#         print(num_1 + num_2)
#     elif opcion == '2':
#         print(num_1 - num_2)
#     elif opcion == '3':
#         print(num_1 * num_2)
#     elif opcion == '4':
#         bandera = False
#         # print('No vimo, gracias por usar mis servicios.')
#         # break
#     else:
#         print('La opcion no es correcta, vuelva a intentarlo.')
# else:
#     print('No vimo, gracias por usar mis servicios.')


###############################################################################
###############################################################################


# if condicion:
#     ...
# asd
# asd
# assertdas
# delattrsd

###############################################################################
###############################################################################

# Hasta el exit

# Solicitar al usuario numeros enteros para sumarlos.
# Para finalizar la ejecución del programa, el usuario debe 
# escribir la palabra exit. El programa debe validar dicha 
# acción y dejar de solicitar numeros. 

# Finalmente, el algoritmo debe mostrar la suma obtenida.

# bandera = True
# suma = 0
# while bandera:
#     numero_string = input('Ingrese numero a sumar:')
#     if numero_string == 'exit':
#         bandera = False
#     else:
#         suma += int(numero_string)

# print('La suma da', suma)

###############################################################################
###############################################################################

# El total o exit?

# Solicitar al usuario la cantidad de numeros enteros a sumar.
# Luego permitirle ingresarlos uno por uno hasta que se ingresen todos 
# o el usuario escriba la palabra ‘exit’.  
# El programa debe validar que se ingreso ‘exit’ y dejar de solicitar numeros. 

# Finalmente, el algoritmo debe mostrar la suma obtenida con un mensaje que 
# resalte si fue total la carga de datos o parcial (debido al ingreso de ‘exit’).

# numeros_a_ingresar = int(input('Ingrese cantidad de numeros a sumar: '))
# suma = 0
# for i in range(numeros_a_ingresar):
#     numero_string = input('Ingrese numero a sumar:')
#     if numero_string == 'exit':
#         print('La suma parcial da', suma)
#         break
#     else:
#         suma += int(numero_string)
# else:
#     print('La suma total da', suma)

###############################################################################
###############################################################################

# La media

# Escribe un programa que pida al usuario cuantos números quiere introducir.
# Luego lee todos los números, guardandolos en una lista, y realiza una media 
# aritmética de todos los valores.

# 🖐 Ayuda: Puedes utilizar la funciones sum() entre parentesis se le pasa un
# iterable (lista, tupla, range) y devuelve la suma de todos sus 
# elementos (sirve solo con valores numericos)

cant_num = int(input('Ingrese cantidad de numeros a calcular: '))
algo = 0
lista = []
while algo < cant_num:
    algo += 1
    numero = int(input('Ingrese numero a sumar: '))
    lista.append(numero)

print(sum(lista)/cant_num)