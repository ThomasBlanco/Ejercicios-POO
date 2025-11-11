from modelo_vehiculo import Vehiculo

class Volqueta(Vehiculo):
    def __init__(self, modelo, color, motor, puertas, pasajeros, combustible, carga):
        super().__init__(modelo, color, motor, puertas, pasajeros, combustible)
        self.carga = carga  # Capacidad de carga en toneladas

    def mostrar_info(self):
        return (
            super().mostrar_info() +
            f"\nCapacidad de carga: {self.carga} toneladas"
        )

