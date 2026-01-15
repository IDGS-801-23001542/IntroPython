'''     operacion de multiplicacion de a x b utilizando sumas
a=3
b=4
salida: 3+3+3+3=12  '''

a = 3
b = 4

resultado = 0
operacion = ""

x = 0
while x < b:
    resultado += a
    operacion += str(a)
    if x < b - 1:
        operacion += "+"
    x += 1

operacion += "=" + str(resultado)

print(operacion)
