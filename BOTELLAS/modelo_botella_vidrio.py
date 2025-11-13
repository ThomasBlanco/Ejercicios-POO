from modelo_botella import Botella  

class Botella_vidrio(Botella):
    def __init__(self, capacidad=850, color="Rojo", material="vidrio"):
        super().__init__(
            material=material,
            capacidad=capacidad,
            forma="cilíndrica",
            diseno="liso",
            tapa="rosca",
            grabados="logo grabado"
        )
        self.color = color
        self.reciclable = True
        self.fragil = True
        self.tratado = False  
    
    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color
        self.tratado = True
        print(f" Botella de vidrio ahora es de color {self.color} (tratada).")

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

