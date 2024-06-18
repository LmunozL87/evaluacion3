import funciones as fn


while True:
    
    print("********************")
    print("********MENU********")
    print("********************")
    print("1. Registrar pedido.")
    print("2. Listar los todos los pedidos.")
    print("3. Imprimir hoja de ruta.")
    print("4. Salir del programa.")

    seleccion = int(input("Seleccione una opción entre 1 y 4: "))      
    if seleccion == 1:
        fn.registrarPedido()
    elif seleccion == 2:
        fn.listarPedidos()
    elif seleccion == 3:
        fn.hojaDeRuta()
    elif seleccion == 4:
        print("Ha salido del programa con éxito.")
        break
    else:
        print("Opción inválida. Reintente con una opción entre 1 y 4.")