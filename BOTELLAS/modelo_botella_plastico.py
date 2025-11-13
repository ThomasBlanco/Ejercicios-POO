from modelo_botella import Botella  

class Botella_plastico(Botella):
    def __init__(self, capacidad=1000, color="Transparente", material="plástico"):
        super().__init__(
            material=material,
            capacidad=capacidad,
            forma="cilíndrica",
            diseno="estriado",
            tapa="rosca",
            grabados="etiqueta impresa"
        )
        self.color = color
        self.reciclable = True
        self.fragil = False
        self.tratado = False

    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color
        self.tratado = True
        print(f" Botella de plástico ahora es de color {self.color} (tratada).")

    def obtener_info(self):
        reciclable = "sí" if self.reciclable else "no"
        fragil = "frágil" if self.fragil else "resistente"
        tratado = "tratada" if self.tratado else "sin tratar"
        return (
            f"Botella de {self.material} - Capacidad: {self.capacidad} ml - "
            f"Color: {self.color}\n"
            f"Reciclable: {reciclable} - {fragil} - {tratado}\n"
            f"Forma: {self.forma}, Diseño: {self.diseno}, "
            f"Tapa: {self.tapa}, Grabados: {self.grabados}"
        )

    def __str__(self):
        return self.obtener_info()
