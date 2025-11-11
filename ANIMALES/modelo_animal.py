class Animal:
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamaño = tamaño
        self.color = color

    # Métodos base
    def moverse(self):
        return f"{self.nombre} se está moviendo en su hábitat ({self.habitat})."

    def comunicarse(self):
        return f"{self.nombre} está comunicándose con otros animales."

    def reproducirse(self):
        return f"{self.nombre} está en época de reproducción."

    def alimentarse(self):
        return f"{self.nombre} se alimenta con dieta {self.dieta}."

    def descansar(self):
        return f"{self.nombre} está descansando."

    def mostrar_info(self):
        return (
            f"Nombre: {self.nombre} | Edad: {self.edad} años | Hábitat: {self.habitat}\n"
            f"Dieta: {self.dieta} | Tamaño: {self.tamaño} | Color: {self.color}"
        )

