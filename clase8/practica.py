# hobies = input('Ingresa tus 3 hobies favoritos separados por un espacio:')
# archivo_abierto = open('miHobbieFavorito.txt', 'a')
# archivo_abierto.write(hobies)
# archivo_abierto.close()


'''
[
    {
        nombre: 'nombre1',
        dni: 123
    },
    {
        nombre: 'nombre2',
        dni: 345
    },
    {
        nombre: 'nombre3',
        dni: 12345343
    },
]
'''
import json

def agendar():
    nombre = input('Ingrese su nombre: ')
    dni = input('Ingrese su dni: ')
    try:
        abierto_lectura = open('datos.json', 'r')
        datos = json.load(abierto_lectura)
        abierto_lectura.close()
    except:
        datos = []
    datos.append({'nombre': nombre, 'dni': dni})
    abierto_escritura = open('datos.json', 'w')
    json.dump(datos, abierto_escritura, indent=4)
    abierto_escritura.close()

def ver_contacto():
    nombre = input('Ingrese su nombre: ')
    with open('datos.json', 'r') as abierto_lectura:
        datos = json.load(abierto_lectura)
        for dato in datos:
            if dato['nombre'] == nombre:
                print(dato['dni'])

def menu():
  print('''Menu
  1. Agendar contacto.
  2. Ver contacto.
  ''')
  opcion = input('Ingrese opcion: ')
  if opcion not in ['1','2']:
    print('No ingreso ninguna opcion valida.')
    return
  if opcion == '1':
    agendar()
  elif opcion == '2':
    ver_contacto()

menu()