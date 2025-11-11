from modelo_animal import Animal

class Caballo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, raza, velocidad):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.raza = raza
        self.velocidad = velocidad  # km/h

    def relinchar(self):
        return f"{self.nombre} está relinchando."

    def moverse(self):
        return f"{self.nombre} está galopando a {self.velocidad} km/h."

    def mostrar_info(self):
        return (
            super().mostrar_info() +
            f"\nRaza: {self.raza} | Velocidad: {self.velocidad} km/h"
        )
