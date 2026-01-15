def suma():
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    print("Resultado:", a + b)

def resta():
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    print("Resultado:", a - b)

def multiplicacion():
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    print("Resultado:", a * b)

def division():
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    if b == 0:
        print("Error: no se puede dividir entre cero")
    else:
        print("Resultado:", a / b)

def menu():
    print("--- MENÚ ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

opcion = 0

while opcion != 5:
    menu()
    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
        suma()
    elif opcion == 2:
        resta()
    elif opcion == 3:
        multiplicacion()
    elif opcion == 4:
        division()
    elif opcion == 5:
        print("Programa finalizado.")
    else:
        print("Opción no válida, intenta de nuevo.")
