from modelo_animal import Animal

class Pato(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, plumas, volador):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.plumas = plumas
        self.volador = volador  # True/False

    def moverse(self):
        return f"{self.nombre} nada y vuela cortas distancias."

    def comunicarse(self):
        return f"{self.nombre} hace 'cuac cuac'."

    def mostrar_info(self):
        return (
            super().mostrar_info() +
            f"\nPlumas: {self.plumas} | Volador: {'Sí' if self.volador else 'No'}"
        )
