from modelo_botella import Botella
from modelo_botella_vidrio import Botella_vidrio
from modelo_botella_plastico import Botella_plastico

class BaseDatos:
    def __init__(self):
        self.botellas = []

    def agregar_botella(self):
        print("\n--- AGREGAR BOTELLA ---")
        tipo = input("Tipo (normal/vidrio/plástico): ").strip().lower()

        if tipo == "vidrio":
            color = input("Color del vidrio: ") or "Rojo"
            capacidad = int(input("Capacidad (ml): ") or 850)
            nueva = Botella_vidrio(capacidad, color)
        elif tipo == "plástico" or tipo == "plastico":
            color = input("Color del plástico: ") or "Transparente"
            capacidad = int(input("Capacidad (ml): ") or 1000)
            nueva = Botella_plastico(capacidad, color)
        else:
            material = input("Material: ")
            capacidad = int(input("Capacidad (ml): "))
            forma = input("Forma: ")
            diseno = input("Diseño: ")
            tapa = input("Tipo de tapa: ")
            grabados = input("Grabados (sí/no o descripción): ")
            nueva = Botella(material, capacidad, forma, diseno, tapa, grabados)

        self.botellas.append(nueva)
        print(f"\n Botella agregada:\n{nueva.obtener_info()}")

    def mostrar_botellas(self):
        print("\n--- LISTA DE BOTELLAS ---")
        if not self.botellas:
            print(" No hay botellas registradas.")
        else:
            for i, b in enumerate(self.botellas):
                print(f"\n[{i+1}] {b.obtener_info()}")

    def acciones_botella(self):
        self.mostrar_botellas()
        if not self.botellas:
            return
        try:
            indice = int(input("\nSeleccione el número de la botella: ")) - 1
            botella = self.botellas[indice]
        except (ValueError, IndexError):
            print(" Índice no válido.")
            return

        print(f"\n ACCIONES DE LA BOTELLA DE {botella.material.upper()} 🔹")
        print(botella.contener_liquidos())
        print(botella.facilitar_el_vertido())
        print(botella.cierre_hermetico())
        print(botella.transporte())
        print(botella.obtener_capacidad())

    def eliminar_botella(self):
        self.mostrar_botellas()
        if not self.botellas:
            return
        try:
            indice = int(input("\nIngrese el número a eliminar: ")) - 1
            eliminada = self.botellas.pop(indice)
            print(f"\n Eliminada: {eliminada.material} ({eliminada.color})")
        except (ValueError, IndexError):
            print(" Índice no válido.")
