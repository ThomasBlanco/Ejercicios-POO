from modelo_vehiculo import Vehiculo
from modelo_carro import Carro
from modelo_microvan import Microvan
from modelo_volqueta import Volqueta

class BaseDatosVehiculos:
    def __init__(self):
        self.vehiculos = []

    # ---------- C (CREAR) ----------
    def agregar_vehiculo(self):
        print("\n--- AGREGAR VEHÍCULO ---")
        tipo = input("Tipo (vehiculo/carro/microvan/volqueta): ").strip().lower()

        modelo = input("Modelo: ")
        color = input("Color: ")
        motor = input("Motor: ")
        puertas = int(input("Número de puertas: "))
        pasajeros = int(input("Capacidad de pasajeros: "))
        combustible = input("Tipo de combustible: ")

        if tipo == "carro":
            tipo_carro = input("Tipo de carro (sedán, deportivo, SUV, etc.): ")
            nuevo = Carro(modelo, color, motor, puertas, pasajeros, combustible, tipo_carro)

        elif tipo == "microvan":
            empresa = input("Empresa de transporte: ")
            placa = input("Placa: ")
            tipo_servicio = input("Tipo de servicio (público/privado): ")
            nuevo = Microvan(modelo, color, motor, puertas, pasajeros, combustible, empresa, placa, tipo_servicio)

        elif tipo == "volqueta":
            carga = float(input("Capacidad de carga (toneladas): "))
            nuevo = Volqueta(modelo, color, motor, puertas, pasajeros, combustible, carga)

        else:
            nuevo = Vehiculo(modelo, color, motor, puertas, pasajeros, combustible)

        self.vehiculos.append(nuevo)
        print(f"\n Vehículo agregado correctamente: {modelo}")

    # ---------- R (LEER) ----------
    def mostrar_vehiculos(self):
        print("\n--- LISTA DE VEHÍCULOS ---")
        if not self.vehiculos:
            print("No hay vehículos registrados.")
        else:
            for i, v in enumerate(self.vehiculos):
                print(f"\n[{i}] {v.mostrar_info()}")

    # ---------- U (ACTUALIZAR) ----------
    def actualizar_vehiculo(self):
        print("\n--- ACTUALIZAR VEHÍCULO ---")
        self.mostrar_vehiculos()
        if not self.vehiculos:
            return
        try:
            indice = int(input("\nIngrese el número del vehículo a actualizar: "))
            vehiculo = self.vehiculos[indice]

            print(f"\nActualizando {vehiculo.modelo}...")
            vehiculo.color = input("Nuevo color: ") or vehiculo.color
            vehiculo.motor = input("Nuevo motor: ") or vehiculo.motor
            vehiculo.combustible = input("Nuevo combustible: ") or vehiculo.combustible

            print(f"\n Vehículo {vehiculo.modelo} actualizado correctamente.")
        except (ValueError, IndexError):
            print(" Índice no válido.")

    # ---------- D (ELIMINAR) ----------
    def eliminar_vehiculo(self):
        print("\n--- ELIMINAR VEHÍCULO ---")
        self.mostrar_vehiculos()
        if not self.vehiculos:
            return
        try:
            indice = int(input("\nIngrese el número del vehículo a eliminar: "))
            eliminado = self.vehiculos.pop(indice)
            print(f"\n Vehículo {eliminado.modelo} eliminado correctamente.")
        except (ValueError, IndexError):
            print(" Índice no válido.")
