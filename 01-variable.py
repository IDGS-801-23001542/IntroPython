'''
Docstring for 01-variable
Una variable es un espacio en memoria que se utiliza para almacenar datos.
En Python no es necesario especificar el tipo de dato, ya que se asigna automáticamente.
Ejemplos de datos que se pueden guardar en variables: números, texto y valores lógicos.
'''

print("Hello, World!")

num1 = 10
num2= 20
sum_result = num1 + num2
print("The sum of", num1, "and", num2, "is:", sum_result)

num3=input("Enter a number: ")
print("you entered:", num3)

num4=input("Enter a number: ")
print("You entered: ", num4)
suma2 = int(num3) + int(num4)
print("La suma de {} + {} es: {}".format(num3,num4,suma2) )