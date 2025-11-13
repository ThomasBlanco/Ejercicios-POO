from modelo_base_datos import BaseDatosVehiculos

def main():
    bd = BaseDatosVehiculos()

    while True:
        print("\n===== MENÚ DE VEHÍCULOS =====")
        print("1. Agregar vehículo")
        print("2. Mostrar vehículos")
        print("3. Actualizar vehículo")
        print("4. Eliminar vehículo")
        print("5. Acciones de vehículo (arrancar, apagar, acelerar, frenar)")
        print("6. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            bd.agregar_vehiculo()

        elif opcion == "2":
            bd.mostrar_vehiculos()

        elif opcion == "3":
            bd.actualizar_vehiculo()

        elif opcion == "4":
            bd.eliminar_vehiculo()

        elif opcion == "5":
            # Submenú de acciones sobre un vehículo existente
            if not bd.vehiculos:
                print("\n No hay vehículos registrados.")
                continue

            bd.mostrar_vehiculos()
            try:
                indice = int(input("\nSeleccione el número del vehículo: "))
                vehiculo = bd.vehiculos[indice]
            except (ValueError, IndexError):
                print(" Índice no válido.")
                continue

            while True:
                print(f"\n ACCIONES PARA: {vehiculo.modelo}")
                print("1. Arrancar")
                print("2. Apagar")
                print("3. Acelerar")
                print("4. Frenar")
                print("5. Volver al menú principal")

                accion = input("Seleccione una acción: ")

                if accion == "1":
                    print(vehiculo.arrancar())
                elif accion == "2":
                    print(vehiculo.apagar())
                elif accion == "3":
                    print(vehiculo.acelerar())
                elif accion == "4":
                    print(vehiculo.frenar())
                elif accion == "5":
                    break
                else:
                    print(" Acción no válida.")

        elif opcion == "6":
            print("\n Saliendo del programa...")
            break

        else:
            print("\n Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()

