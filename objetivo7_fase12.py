#Juan Manuel Dominguez García

class Vehiculo:
    def __init__(self, marca, velocidad=0):
        self.marca = marca
        self.velocidad = velocidad

    def acelerar(self, v):
        self.velocidad += v

    def desacelerar(self, v):
        if self.velocidad - v >= 0:
            self.velocidad -= v
        else:
            self.velocidad = 0

    def mostrar_velocidad(self):
        print("La velocidad actual es:", self.velocidad, "km/h")


class Coche(Vehiculo):
    def __init__(self, marca, velocidad=0, bocina="tuuut"):
        super().__init__(marca, velocidad)
        self.bocina = bocina

    def tocar_claxon(self):
        print(self.bocina)


# Ejemplo de uso
mi_coche = Coche("Toyota")
mi_coche.acelerar(50)
mi_coche.mostrar_velocidad()
mi_coche.desacelerar(20)
mi_coche.mostrar_velocidad()
mi_coche.tocar_claxon()