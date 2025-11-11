from modelo_vehiculo import Vehiculo

class Carro(Vehiculo):
    def __init__(self, modelo, color, motor, puertas, pasajeros, combustible, tipo):
        super().__init__(modelo, color, motor, puertas, pasajeros, combustible)
        self.tipo = tipo  # Ejemplo: deportivo, sedán, SUV

    def mostrar_info(self):
        return (
            super().mostrar_info() +
            f"\nTipo de carro: {self.tipo}"
        )

