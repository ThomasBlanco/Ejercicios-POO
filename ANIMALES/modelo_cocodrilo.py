from modelo_animal import Animal

class Cocodrilo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, longitud, fuerza_mandibula):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.longitud = longitud
        self.fuerza_mandibula = fuerza_mandibula  # N o psi

    def moverse(self):
        return f"{self.nombre} se desliza sigilosamente por el agua."

    def comunicarse(self):
        return f"{self.nombre} emite sonidos graves para comunicarse."

    def mostrar_info(self):
        return (
            super().mostrar_info() +
            f"\nLongitud: {self.longitud} m | Fuerza de mandíbula: {self.fuerza_mandibula} N"
        )
