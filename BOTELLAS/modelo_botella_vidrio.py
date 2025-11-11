from modelo_botella import Botella  

class Botella_vidrio(Botella):
    def __init__(self, capacidad=850, color="Rojo", material="vidrio"):
        # Llamamos al constructor de la clase padre
        super().__init__(
            material=material,
            capacidad=capacidad,
            forma="cilíndrica",
            diseno="liso",
            tapa="rosca",
            grabados="logo grabado"
        )

        # Atributos adicionales propios de la botella de vidrio
        self.color = color
        self.reciclable = True
        self.fragil = True
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
