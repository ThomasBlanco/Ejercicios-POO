from modelo_botella import Botella  

class Botella_plastico(Botella):
    def __init__(self, capacidad=1000, color="Transparente", material="plástico"):
        # Llamamos al constructor de la clase padre
        super().__init__(
            material=material,
            capacidad=capacidad,
            forma="cilíndrica",
            diseno="estriado",
            tapa="rosca",
            grabados="etiqueta impresa"
        )

        # Atributos adicionales propios de la botella de plástico
        self.color = color
        self.reciclable = True
        self.fragil = False
        self.tratado = False
    
    def obtener_capacidad(self):
        return self.capacidad
    
    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color
        self.tratado = True
    
    def obtener_info(self):
        reciclable = "sí" if self.reciclable else "no"
        fragil = "frágil" if self.fragil else "resistente"
        tratado = "tratada" if self.tratado else "sin tratar"
        return (
            f"Botella de {self.material} - Capacidad: {self.capacidad} ml - "
            f"Color: {self.color}\n"
            f"Reciclable: {reciclable} - {fragil} - {tratado}"
        )

    def es_reciclable(self):
        return self.reciclable

    def es_fragil(self):
        return self.fragil