class Vehiculo:
    def __init__(self, modelo, color, motor, puertas, pasajeros, combustible):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.puertas = puertas
        self.pasajeros = pasajeros
        self.combustible = combustible
        self.encendido = False

    def arrancar(self):
        self.encendido = True
        return f"{self.modelo} ha arrancado."

    def apagar(self):
        self.encendido = False
        return f"{self.modelo} se ha apagado."

    def acelerar(self):
        if self.encendido:
            return f"{self.modelo} está acelerando..."
        else:
            return f"{self.modelo} no puede acelerar porque está apagado."

    def frenar(self):
        return f"{self.modelo} está frenando."

    def mostrar_info(self):
        return (
            f"Modelo: {self.modelo} | Color: {self.color}\n"
            f"Motor: {self.motor} | Puertas: {self.puertas}\n"
            f"Pasajeros: {self.pasajeros} | Combustible: {self.combustible}"
        )
