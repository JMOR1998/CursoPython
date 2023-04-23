'''Enunciado:
Escribir un programa que realice la siguiente operación:
   3 + 2
( ------- )²
   2 . 5
'''
# 1@ Forma de resolverlo
#print(((3 + 2) / (2 * 5)) ** 2) 

# 2@ Forma de resolverlo con una variable
calculo = (((3+2) / (2*5)) ** 2)
#print(calculo)

# 3@ Forma de resolverlo con funciones matemáticas importadas en python
calculo = pow(((3 + 2) / (2 * 5)) , 2)
#print(calculo)

# El resultado es 0.25
print("El resultado de la operación es: ", calculo)