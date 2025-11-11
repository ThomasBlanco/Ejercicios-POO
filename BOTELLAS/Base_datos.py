class Base_dato:
    def __init__(self):
        self.lista_botellas = []

    def agregar_botella(self, obj_botella):
        """Agrega una botella individual a la lista."""
        self.lista_botellas.append(obj_botella)

    def extender_lista(self, lista_botellas):
        """Agrega varias botellas a la lista."""
        self.lista_botellas.extend(lista_botellas)

    def eliminar_objeto(self, dato_index):
        """Elimina una botella por su índice."""
        if 0 <= dato_index < len(self.lista_botellas):
            self.lista_botellas.pop(dato_index)
            print(" Botella eliminada correctamente.")
        else:
            print(" Índice inválido. No se eliminó ninguna botella.")

    def imprimir_info(self):
        """Muestra información de todas las botellas almacenadas."""
        if not self.lista_botellas:
            print(" No hay botellas registradas.")
        else:
            print("\n Lista de botellas registradas:")
            for i, botella in enumerate(self.lista_botellas):
                print(f"\n Botella #{i + 1}")
                print(f"Material: {botella.material}")
                print(f"Capacidad: {botella.capacidad} ml")
                print(f"Forma: {botella.forma}")
                print(f"Tapa: {botella.tapa}")
