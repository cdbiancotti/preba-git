# def prueba(*args):
#     return args

# print(prueba(1,2,3,4,'pepito',6,7,8,9))
# print(prueba(1,2,3,4,5,6))
# print(prueba(1,2,3))

# def prueba(**kwargs):
#     return kwargs

# print(prueba(valor1=1,valor2=2,ricardone=3,fort=4,hola='pepito'))
# print(prueba(1,2,3,4,5,6))
# print(prueba(1,2,3))


# def sumar(valor1=0, valor2=0, valor3=0):
#     print(valor1 + valor2 + valor3)
    
# sumar(1,2,3)
# sumar(5,19)
# sumar()
# sumar(1,2,3,4,5,6)


# def sumar(*valores):
#     print(sum(valores))
    
# sumar(1,2,3)
# sumar(5,3,4,5,619)
# sumar(3,4,5,6,3,4,5,6,3,4,5,6)
# sumar(1,2,3,4,5,6,3,4,5,6,3,4,5,6,3,4,5,6,3,4,5,6,3,4,5,6,3,4,5,6,3,4,5,6)

# ============================================================================
# ============================================================================

# def saludar(ciudad):
#     print(f'¡Hola, te damos la bienvenida a {ciudad}!')

# saludar(input('Ingrese una ciudad'))

# ============================================================================
# ============================================================================

# print(len('asd'))
# print(len([1,2,3,4]))

# def mi_len(coleccion_de_datos):
#     contador_de_valores = 0
#     for valor in coleccion_de_datos:
#         contador_de_valores += 1
#     # return contador_de_valores
#     print(contador_de_valores)

# # print(mi_len('asd'))
# # print(mi_len([1,2,3,4]))


# mi_len('asd')
# mi_len([1,2,3,4])
    
# # contador_de_valores = 0
# # for valor in 'asd':
# #     contador_de_valores += 1
    
# # print(contador_de_valores)


# # contador_de_valores = 0
# # for valor in [1,2,3,4]:
# #     contador_de_valores += 1
    
# # print(contador_de_valores)

# ============================================================================
# ============================================================================

# def serie_de_numeros(lista1):
#     return sum(lista1)/len(lista1)

# resultado = serie_de_numeros([1,2,3,4,5])

# print(resultado)

# ============================================================================
# ============================================================================

# def anio_bisiesto(anio):
    
#     for caracter in anio:
#         if caracter not in '0123456789':
#             print('Ingrese un numero.')
#             return
            
#     anio = int(anio)
    
#     if anio%4==0 and (anio%100==1 or anio%400==0):
#         print(f'El año {anio} es bisiesto')
#     else:
#         print(f'El año {anio} no es bisiesto')

    
# valor = input('Ingrese un anio a chequear: ')
# anio_bisiesto(valor)

# ============================================================================
# ============================================================================

def separar(valores, lista1, lista2):
    valores.sort()
    for valor in valores:
        if valor%2==0:
            lista1.append(valor)
        else:
            lista2.append(valor)


lista_pares = []
lista_impares = []
separar([1,2,15,3,4,5,6], lista_pares, lista_impares)

print(lista_pares)
print(lista_impares)