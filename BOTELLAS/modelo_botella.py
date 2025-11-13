class Botella:
    def __init__(self, material, capacidad, forma, diseno, tapa, grabados):
        self.material = material
        self.capacidad = capacidad
        self.forma = forma
        self.diseno = diseno
        self.tapa = tapa
        self.grabados = grabados
        self.reciclable = True
        self.fragil = True
        self.tratado = False
        self.color = "Transparente"

    # ---------- FUNCIONES ----------
    def contener_liquidos(self):
        return " Los líquidos están contenidos dentro del recipiente."

    def facilitar_el_vertido(self):
        return " Facilita el vertido mediante su cuello o embudo."

    def cierre_hermetico(self):
        return " Posee un cierre hermético gracias a su tapa."

    def transporte(self):
        return " Puede transportarse en cajas o estuches."

    def obtener_capacidad(self):
        return f"Capacidad total: {self.capacidad} ml."

    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color
        self.tratado = True
        print(f" Color cambiado a {self.color} (botella tratada).")

    # ---------- INFO ----------
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

    def __str__(self):
        return self.obtener_info()
