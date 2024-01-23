class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def imprimir(self):
        print(f'{self.nombre} {self.nota}')
    
VALOR_PREDETERMINADO = 'PEPITO GRILLO'