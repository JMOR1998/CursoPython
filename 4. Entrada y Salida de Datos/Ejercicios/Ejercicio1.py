'''Enunciado
Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, sabiendo que la formula general es la que está en la imagen, el usuario debe ingresar los valores de “a”, “b” y “c”, y el programa debe hacer el proceso para que al final muestre el mensaje: “La solución es: <solucion>”
'''
a = int(input("Ingrese el valor de \"A\": "))
b = int(input("Ingrese el valor de \"B\": "))
c = int(input("Ingrese el valor de \"C\": "))
# 1@ Solución a la hora de realizar la raiz cuadrada, sabiendo que una raiz cuadrada es elevando a 1/2, una raiz cúbica es elevando a 1/3...
resultado1 = (((b*-1) + (((b**2)-(4*a*c))**0.5)) / (2*a))
resultado2 = (((b*-1) - (((b**2)-(4*a*c))**0.5)) / (2*a))
print("La primera solución es: ",resultado1)
print("La segunda solución es: ",resultado2)
# 2@ Solución a la hora de realizar la raiz cuadrada con la funcion importada sqrt
from math import sqrt
resultado3 = (((b*-1) + (sqrt((b**2)-(4*a*c)))) / (2*a))
resultado4 = (((b*-1) - (sqrt((b**2)-(4*a*c)))) / (2*a))
print("La primera solución es: ",resultado3)
print("La segunda solución es: ",resultado4)
