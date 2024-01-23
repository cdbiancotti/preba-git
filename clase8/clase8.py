class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def imprimir(self):
        print(f'{self.nombre} {self.nota}')
    
    def __str__(self):
        return f'{self.nombre} {self.nota}'

def gritar():
    print('AAAAAAAAAAAAAAAAAAAAAAAAAAHHH!!!!')
    
VALOR_PREDETERMINADO = 'PEPITO GRILLO'