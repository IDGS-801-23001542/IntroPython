'''
Docstring for practica4
pedir al usuario que ingrese 20 numero repetidos y sin repetir
los almacene en una lista y luego muestre la lista ordenada de menor a mayor,
tambien nos diga cuantos son repetidos y cuantas veces se repitieron
separalos entre pareales e impares
'''
numeros = []

# Pedir 20 números al usuario
for i in range(20):
    num = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(num)

# Mostrar lista original
print("\nLista original:")
print(numeros)

# Ordenar la lista
numeros_ordenados = sorted(numeros)
print("\nLista ordenada de menor a mayor:")
print(numeros_ordenados)

# Contar números repetidos
print("\nNúmeros repetidos y cuántas veces aparecen:")
repetidos = False
for num in set(numeros):
    cantidad = numeros.count(num)
    if cantidad > 1:
        print(f"{num} se repite {cantidad} veces")
        repetidos = True

if not repetidos:
    print("No hay números repetidos")

# Separar pares e impares
pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("\nNúmeros pares:")
print(pares)

print("\nNúmeros impares:")
print(impares)
