from modelo_base_datos import BaseDatos

def main():
    bd = BaseDatos()

    while True:
        print("\n===== MENÚ DE BOTELLAS =====")
        print("1. Agregar botella")
        print("2. Mostrar botellas")
        print("3. Actualizar botella")
        print("4. Eliminar botella")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            bd.agregar_botella()
        elif opcion == "2":
            bd.mostrar_botellas()
        elif opcion == "3":
            bd.actualizar_botella()
        elif opcion == "4":
            bd.eliminar_botella()
        elif opcion == "5":
            print("\n Saliendo del programa...")
            break
        else:
            print(" Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    main()
