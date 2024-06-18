import csv
sectores = ['quilpue','peñablanca','valparaiso']
pedidos = {}


def registrarPedido():
    cant5kg = 0
    cant15kg = 0
    cant45kg = 0

    nombre = input("Ingrese su nombre y apellido: ")
    direccion = input("Ingrese su dirección: ")
    comuna = input("Ingrese su comuna: ")
            


    while True:
        print("Seleccione su cilindro.\n")
        print("1. Cilindro de 5 Kgs.")
        print("2. Cilindro de 15 Kgs.")
        print("3. Cilindro de 45 Kgs.")
        print("4. Volver.")

        opcCilindro = int(input("Seleccione el cilindro que desea comprar: "))
        
        if opcCilindro == 1:
            cant5kg = input("¿Cuántos desea? ")
        elif opcCilindro == 2:
            cant15kg = input("¿Cuántos desea? ")
        elif opcCilindro == 3:
            cant45kg = input("¿Cuántos desea? ")
        elif opcCilindro == 4:
            break
        
    pedidos.update({
        'Cliente' : nombre,
        'Dirección' : direccion,
        'Sector' : comuna,
        'Cil. 5kg' : cant5kg,
        'Cil. 15kg' : cant15kg,
        'Cil 45kg' : cant45kg
    })
        

def listarPedidos():
    for datos in pedidos:
        print(datos)

def hojaDeRuta():
    sector = input("Ingrese su comuna: ").lower

    if sector not in sectores:
        print("Lo sentimos. Nuestros servicios no llegan a su comuna.")
