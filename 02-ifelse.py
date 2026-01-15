"""
Operadores lógicos / relacionales

==  igual
!=  diferente
>   mayor que
<   menor que
>=  mayor o igual que
<=  menor o igual que

Operadores aritméticos

+   suma
-   resta
*   multiplicación
/   división
%   módulo
//  división entera
**  exponente

Operadores lógicos (booleanos)

and  y
or   o
not  no
"""

'''
La estructura if-else se utiliza para tomar decisiones dentro del programa.
Evalúa una condición y ejecuta un bloque de código si la condición es verdadera,
y otro bloque diferente si la condición es falsa.
'''


num1=2
num2=3

if num1 > num2:    
    
    print("{} es mayor que {}".format(num1,num2))
else:
    print("{} es menor que {}".format(num1, num2))