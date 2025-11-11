from modelo_vehiculo import Vehiculo

class Microvan(Vehiculo):
    def __init__(self, modelo, color, motor, puertas, pasajeros, combustible, empresa, placa, tipo):
        super().__init__(modelo, color, motor, puertas, pasajeros, combustible)
        self.empresa = empresa
        self.placa = placa
        self.tipo = tipo  # Ejemplo: público o privado

    def mostrar_info(self):
        return (
            super().mostrar_info() +
            f"\nEmpresa: {self.empresa} | Placa: {self.placa} | Tipo: {self.tipo}"
        )


