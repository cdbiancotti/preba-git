class Televisor:

    colores_disponibles = ['blanco', 'negro', 'rojo', 'azul', 'gris']
    niveles_y_precios_de_consumo = {
        'A': 100,
        'B': 80,
        'C': 60,
        'D': 50,
        'E': 30, 
        'F': 10
    }

    def __init__(self, precio_base=100, color='blanco', consumo_e='F', peso='5'):
        self.precio_base = precio_base
        self.color = self.__comprobar_color(color.lower())
        self.consumo_e = self.__comprobar_consumo(consumo_e)
        self.peso = peso
    
    def __comprobar_consumo(self, valor_consumo):
        return valor_consumo if valor_consumo in self.niveles_y_precios_de_consumo.keys() else 'F'
    
    def __comprobar_color(self, valor_color):
        return valor_color if valor_color in self.colores_disponibles else 'blanco'

    def obtener_precio_final(self):
        nivel_consumo = self.consumo_e
        precio_segun_consumo = self.niveles_y_precios_de_consumo.get(nivel_consumo)
        precio_final = self.precio_base + precio_segun_consumo
        
        if 0 < self.peso <= 19:
            precio_peso = 10
        elif 20 < self.peso <= 49:
            precio_peso = 50
        elif 50 < self.peso <= 79:
            precio_peso = 80
        elif 80 <= self.peso:
            precio_peso = 100
        
        return precio_final + precio_peso

def calcular_precio_total_de_la_compra(listado_de_televisores):
    precio_total = 0
    for tele in listado_de_televisores:
        precio_total += tele.obtener_precio_final()
    return precio_total


televisores = [
    Televisor(250,'rojo', 'E', 10),
    Televisor(143,'negro', 'C', 13),
    Televisor(54,'gris', 'A', 7),
    Televisor(300,'violeta', 'B', 23),
]

print(calcular_precio_total_de_la_compra(televisores))