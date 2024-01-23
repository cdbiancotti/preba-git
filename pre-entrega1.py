base_de_datos = {}

def almacenar():
    usuario = input('Usuario: ')
    contrasenia = input('Contrasenia: ')
    base_de_datos[usuario] = contrasenia

def mostrar():
    usuario_buscado = input('Ingrese usuario a buscar: ')
    for usuario in base_de_datos:
        if usuario_buscado in usuario:
            print(usuario)

def login(user, contra):
    # v1
    contrasenia = base_de_datos.get(user)
    if contrasenia:
        print('Usuario erroneo.')
        return
    
    # v2
    # try:
    #     contrasenia = base_de_datos[user]
    # except:
    #     print('Usuario erroneo.')
    #     return

    # v1, v2
    if contrasenia == contra:
        print(f'Iniciaste sesion correctamente {user}!')
    else:
        print(f'La contrasenia utilizada {contra} no es correcta para el usuario {user}')
        
while True:
  opcion = input('''
  1. Registrar usuario
  2. Mostrar usuarios
  3. Iniciar sesion
  4. Salir
  ''')
  if opcion == '1':
    almacenar()
  elif opcion == '2':
    mostrar()
  elif opcion == '3':
    usuario = input('Usuario: ')
    contrasenia = input('Contrasenia: ')
    login(usuario, contrasenia)
  elif opcion == '4':
    print('Vuelva prontos')
    break
  else:
    print('No es una opcion valida. Vuelva a intentarlo.')