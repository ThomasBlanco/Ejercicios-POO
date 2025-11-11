from modelo_botella import Botella


class BaseDatos:
    def __init__(self):
        self.botellas = []  # lista que simula la base de datos

    # ---------- C: CREAR / AGREGAR ----------
    def agregar_botella(self):
        print("\n--- AGREGAR BOTELLA ---")
        material = input("Material: ")
        capacidad = int(input("Capacidad (ml): "))
        forma = input("Forma: ")
        diseno = input("Diseño: ")
        tapa = input("Tipo de tapa: ")
        grabados = input("Grabados (sí/no o descripción): ")

        nueva_botella = Botella(material, capacidad, forma, diseno, tapa, grabados)
        self.botellas.append(nueva_botella)
        print(f"\n Botella agregada correctamente: {nueva_botella.obtener_info()}")

    # ---------- R: LEER / MOSTRAR ----------
    def mostrar_botellas(self):
        print("\n--- LISTA DE BOTELLAS ---")
        if not self.botellas:
            print("No hay botellas registradas.")
        else:
            for i, botella in enumerate(self.botellas):
                print(f"\n{i+1}. {botella.obtener_info()}")

    # ---------- U: ACTUALIZAR ----------
    def actualizar_botella(self):
        print("\n--- ACTUALIZAR BOTELLA ---")
        self.mostrar_botellas()
        if not self.botellas:
            return
        
        try:
            indice = int(input("\nIngrese el número de la botella a actualizar: ")) - 1
            if 0 <= indice < len(self.botellas):
                botella = self.botellas[indice]
                print(f"Seleccionada: {botella.obtener_info()}")

                # Permitir actualizar atributos opcionales
                nuevo_color = input("Nuevo color (enter para no cambiar): ")
                if nuevo_color:
                    botella.cambiar_color(nuevo_color)

                nuevo_diseno = input("Nuevo diseño (enter para no cambiar): ")
                if nuevo_diseno:
                    botella.diseno = nuevo_diseno

                nueva_tapa = input("Nuevo tipo de tapa (enter para no cambiar): ")
                if nueva_tapa:
                    botella.tapa = nueva_tapa

                print(f"\n Botella actualizada correctamente: {botella.obtener_info()}")
            else:
                print(" Índice fuera de rango.")
        except ValueError:
            print(" Entrada inválida.")

    # ---------- D: ELIMINAR ----------
    def eliminar_botella(self):
        print("\n--- ELIMINAR BOTELLA ---")
        self.mostrar_botellas()
        if not self.botellas:
            return
        
        try:
            indice = int(input("\nIngrese el número de la botella a eliminar: ")) - 1
            if 0 <= indice < len(self.botellas):
                eliminada = self.botellas.pop(indice)
                print(f"\n Botella eliminada correctamente: {eliminada.obtener_info()}")
            else:
                print(" Índice fuera de rango.")
        except ValueError:
            print(" Entrada inválida.")
