from modelo_animal import Animal

class Escarabajo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, especie, vuela):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.especie = especie
        self.vuela = vuela  # True/False

    def moverse(self):
        if self.vuela:
            return f"{self.nombre} está volando sobre las hojas."
        else:
            return f"{self.nombre} se arrastra por el suelo."

    def mostrar_info(self):
        return (
            super().mostrar_info() +
            f"\nEspecie: {self.especie} | Vuela: {'Sí' if self.vuela else 'No'}"
        )
