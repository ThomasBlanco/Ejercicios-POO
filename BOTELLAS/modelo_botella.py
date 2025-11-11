class Botella:
    def __init__(self, material, capacidad, forma, diseno, tapa, grabados):
        self.material = material
        self.capacidad = capacidad
        self.forma = forma
        self.diseno = diseno
        self.tapa = tapa
        self.grabados = grabados

        # Atributos adicionales propios de la botella
        self.reciclable = True
        self.fragil = True
        self.tratado = False
        self.color = "Transparente"  # valor por defecto

    # ---------- MÉTODOS FUNCIONALES ----------
    def contener_liquidos(self):
        return "Los líquidos están en el recipiente"

    def facilitar_el_vertido(self):
        return "Embudo"

    def cierre_hermetico(self):
        return "Sí, tiene cierre hermético"

    def transporte(self):
        return "Cajas"

    # ---------- GETTERS Y SETTERS ----------
    def obtener_capacidad(self):
        return self.capacidad

    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color
        self.tratado = True

    # ---------- INFORMACIÓN ----------
    def obtener_info(self):
        reciclable = "sí" if self.reciclable else "no"
        fragil = "frágil" if self.fragil else "resistente"
        tratado = "tratada" if self.tratado else "sin tratar"
        return (
            f"Botella de {self.material} - Capacidad: {self.capacidad} ml - "
            f"Color: {self.color}\n"
            f"Reciclable: {reciclable} - {fragil} - {tratado}\n"
            f"Forma: {self.forma}, Diseño: {self.diseno}, Tapa: {self.tapa}, Grabados: {self.grabados}"
        )

    def es_reciclable(self):
        return self.reciclable

    def es_fragil(self):
        return self.fragil
