from modelo_base_datos import BaseDatosAnimales

def main():
    bd = BaseDatosAnimales()
    while True:
        print("\n===== MENÚ DE ANIMALES =====")
        print("1. Agregar animal")
        print("2. Mostrar animales")
        print("3. Actualizar animal")
        print("4. Eliminar animal")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            bd.agregar_animal()
        elif opcion == "2":
            bd.mostrar_animales()
        elif opcion == "3":
            bd.actualizar_animal()
        elif opcion == "4":
            bd.eliminar_animal()
        elif opcion == "5":
            break
        else:
            print(" Opción inválida.")

if __name__ == "__main__":
    main()


