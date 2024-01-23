# Mitigando el fallo


'''En la función de nuestro ejercicio hay un fallo potencial, averigua cuándo sucede y 
retorna el valor None en ese caso especial, en cualquier otro caso devuelve el resultado normal de la función.

def dividir(a, b):  
 return a/b

Pista: El fallo es aritmetico y se da por un valor que no podria pasarse por el parametro b'''

# def validar(param1, param2):
#     ...

# def dividir(a, b):
#     if validar(a, b):
#         return "B no puede ser igual a cero"
#     elif type(b).__name__ == 'str':
#         return "B no puede ser algo distinto a un numero"
#     elif type(b).__name__ == 'list':
#         return "B no puede ser algo distinto a un numero"
#     else:   
#         return a/b

# def dividir(a, b):
#   try:
#     return a/b
#   except ZeroDivisionError:
#     return "B no puede ser igual a cero"
# #   except:
# #     return 'Hubo un error'
#   except Exception as e:
#     return f'El error encontrado es del tipo: {type(e).__name__}'

# print(dividir(1, 0))


# =========================================================================
# =========================================================================

# Que error genera
'''
Crear un programa que muestre un menu con 4 opciones y, segun la opcion elegida 
por el usuario, muestre el tipo de error que se generaria si se ejecutara ese codigo en python.  

Usa las siguientes opciones:  
1. ‘Soy un string’ - 4
2. 4/0
3. prnt(‘Mostrando codigo’)
4. int(‘Quiero ser un numero’)
'''

print('''Menu
----------------------
1. 'Soy un string' - 4
2. 4/0
3. prnt('Mostrando codigo')
4. int('Quiero ser un numero')
''')
opcion = input('Ingrese opcion: ')
try:
    if opcion == '1':
        'Soy un string' - 4
    elif opcion == '2':
        4/0
    elif opcion == '3':
        prnt('Mostrando codigo')
    elif opcion == '4':
        int('Quiero ser un numero')
    else:
        print('Seleccionaste una opcion inexistente.')
except Exception as error:
    print(type(error).__name__)