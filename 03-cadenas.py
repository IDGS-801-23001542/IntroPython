'''
Docstring for 03-cadenas
CADENAS
Las cadenas son textos que se escriben entre comillas simples o dobles.
Se utilizan para manejar palabras, frases o mensajes dentro del programa.
Python permite concatenar cadenas y acceder a sus caracteres.
'''

texto="desarroyo web profrcional utl"
print(texto)
print(texto.lower)
print(texto.upper)
print(texto.title)
print(texto.find("al"))
print(texto.count("e"))

print(texto.replace("e", "a"))

cadenaSeparada=texto.split(" ")
print(cadenaSeparada)