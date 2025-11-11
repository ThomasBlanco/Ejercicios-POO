from modelo_animal import Animal
from modelo_caballo import Caballo
from modelo_cocodrilo import Cocodrilo
from modelo_pez import Pez
from modelo_escarabajo import Escarabajo
from modelo_pato import Pato

class BaseDatosAnimales:
    def __init__(self):
        self.animales = []  # lista para almacenar los animales

    # --- Crear ---
    def agregar_animal(self):
        print("\n--- AGREGAR ANIMAL ---")
        tipo = input("Tipo (animal/caballo/cocodrilo/pez/escarabajo/pato): ").lower()
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        habitat = input("Hábitat: ")
        dieta = input("Dieta: ")
        tamaño = input("Tamaño: ")
        color = input("Color: ")

        if tipo == "caballo":
            raza = input("Raza: ")
            velocidad = input("Velocidad (km/h): ")
            nuevo = Caballo(nombre, edad, habitat, dieta, tamaño, color, raza, velocidad)
        elif tipo == "cocodrilo":
            longitud = input("Longitud (m): ")
            fuerza = input("Fuerza de mandíbula (N): ")
            nuevo = Cocodrilo(nombre, edad, habitat, dieta, tamaño, color, longitud, fuerza)
        elif tipo == "pez":
            tipo_agua = input("Tipo de agua (dulce/salada): ")
            velocidad_nado = input("Velocidad de nado (km/h): ")
            nuevo = Pez(nombre, edad, habitat, dieta, tamaño, color, tipo_agua, velocidad_nado)
        elif tipo == "escarabajo":
            especie = input("Especie: ")
            habitat_detalle = input("Tipo de ambiente: ")
            nuevo = Escarabajo(nombre, edad, habitat, dieta, tamaño, color, especie, habitat_detalle)
        elif tipo == "pato":
            plumas = input("Tipo de plumas: ")
            volador = input("¿Es volador? (sí/no): ")
            nuevo = Pato(nombre, edad, habitat, dieta, tamaño, color, plumas, volador)
        else:
            nuevo = Animal(nombre, edad, habitat, dieta, tamaño, color)

        self.animales.append(nuevo)
        print(f"\n {tipo.capitalize()} agregado correctamente.")

    # --- Leer ---
    def mostrar_animales(self):
        print("\n--- LISTA DE ANIMALES ---")
        if not self.animales:
            print("No hay animales registrados.")
        else:
            for i, a in enumerate(self.animales):
                print(f"\n[{i}] {a.mostrar_info()}")

    # --- Actualizar ---
    def actualizar_animal(self):
        self.mostrar_animales()
        i = int(input("\nIngrese el número del animal a actualizar: "))
        if 0 <= i < len(self.animales):
            nuevo_color = input("Nuevo color: ")
            self.animales[i].color = nuevo_color
            print(" Animal actualizado correctamente.")
        else:
            print(" Índice no válido.")

    # --- Eliminar ---
    def eliminar_animal(self):
        self.mostrar_animales()
        i = int(input("\nIngrese el número del animal a eliminar: "))
        if 0 <= i < len(self.animales):
            eliminado = self.animales.pop(i)
            print(f" Animal eliminado: {eliminado.nombre}")
        else:
            print(" Índice no válido.")
