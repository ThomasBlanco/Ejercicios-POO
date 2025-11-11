from modelo_base_datos import BaseDatosVehiculos

def main():
    bd = BaseDatosVehiculos()

    while True:
        print("\n===== MENÚ DE VEHÍCULOS =====")
        print("1. Agregar vehículo")
        print("2. Mostrar vehículos")
        print("3. Actualizar vehículo")
        print("4. Eliminar vehículo")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            bd.agregar_vehiculo()
        elif opcion == "2":
            bd.mostrar_vehiculos()
        elif opcion == "3":
            bd.actualizar_vehiculo()
        elif opcion == "4":
            bd.eliminar_vehiculo()
        elif opcion == "5":
            print("\n Saliendo del programa...")
            break
        else:
            print(" Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()

