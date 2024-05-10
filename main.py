from membresia import Membresia, Gratis, Basica, Familiar, SinConexion, Pro

correo = input("Por favor, ingrese el correo: ")
numero_tarjeta = input("Por favor, ingrese el número de tarjeta: ")
usuario = Gratis(correo, numero_tarjeta)
while True:
    print("\nMenú:")
    print("1. Cambiar membresía a Básica")
    print("2. Cambiar membresía a Familiar")
    print("3. Cambiar membresía a Sin Conexión")
    print("4. Cambiar membresía a Pro")
    print("5. Cancelar membresía")
    print("6. Salir")
    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        usuario = usuario.cambiar_suscripcion(1)
        print(f"Membresía cambiada a: {type(usuario).__name__}")
    elif opcion == "2":
        usuario = usuario.cambiar_suscripcion(2)
        print(f"Membresía cambiada a: {type(usuario).__name__}")
    elif opcion == "3":
        usuario = usuario.cambiar_suscripcion(3)
        print(f"Membresía cambiada a: {type(usuario).__name__}")
    elif opcion == "4":
        usuario = usuario.cambiar_suscripcion(4)
        print(f"Membresía cambiada a: {type(usuario).__name__}")
    elif opcion == "5":
        usuario = usuario.cancelar_suscripcion()
        print("Membresía cancelada.")
    elif opcion == "6":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número válido.")
