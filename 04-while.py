'''
Docstring for 04-while
El ciclo while repite un bloque de código mientras una condición sea verdadera.
Se debe tener cuidado de modificar la condición para evitar ciclos infinitos.
'''

tem=""
x=0
while x<10:
    x+=1
    tem+=str(x)+("+")
    
print(tem)

