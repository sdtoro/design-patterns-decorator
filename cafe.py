class Cafe:
    def obtener_precio(self):
        return 10.0

class DecoradorCafe:
    def __init__(self, cafe):
        self._cafe = cafe
    
    def obtener_precio(self):
        return self._cafe.obtener_precio()

class Leche(DecoradorCafe):
    def obtener_precio(self):
        return self._cafe.obtener_precio() + 2.0

class Caramelo(DecoradorCafe):
    def obtener_precio(self):
        return self._cafe.obtener_precio() + 3.0

# Uso
mi_cafe = Cafe()
mi_cafe_con_leche = Leche(mi_cafe)
mi_cafe_con_leche_y_caramelo = Caramelo(mi_cafe_con_leche)

print("Precio de mi café: ", mi_cafe.obtener_precio())
print("Precio de mi café con leche: ", mi_cafe_con_leche.obtener_precio())
print("Precio de mi café con leche y caramelo: ", mi_cafe_con_leche_y_caramelo.obtener_precio())