'''
Docstring for 05-funciones
# Una función es un bloque de código reutilizable que realiza una tarea específica.
# Se define usando la palabra reservada def y puede recibir parámetros.
# Las funciones ayudan a organizar y reutilizar el código.
'''

import os

def saludar(nombre):
    """Funcion que saluda a la persona cuyo nombre se pasa como argumento."""
    return f"Hola, {nombre}!"
def sumar(a, b):
    """Funcion que devuelve la suma de dos numeros."""
    return a + b
os.system("cls")
saludar ("Ana")
os.system("pause")

def main():
    saludar("Juan")
    resultado_suma = sumar(5, 7)
    print("La suma de 5 y 7 es:", resultado_suma)

if __name__=="__main__":
    main()