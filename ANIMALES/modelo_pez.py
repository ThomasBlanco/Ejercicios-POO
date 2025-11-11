from modelo_animal import Animal

class Pez(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, tipo_agua, velocidad_nado):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.tipo_agua = tipo_agua  # dulce o salada
        self.velocidad_nado = velocidad_nado  # km/h

    def moverse(self):
        return f"{self.nombre} nada a {self.velocidad_nado} km/h en agua {self.tipo_agua}."

    def mostrar_info(self):
        return (
            super().mostrar_info() +
            f"\nTipo de agua: {self.tipo_agua} | Velocidad de nado: {self.velocidad_nado} km/h"
        )
