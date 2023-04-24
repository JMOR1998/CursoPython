'''Enunciado:
Hacer un programa que pida al usuario su nombre, su edad y su sexo y los muestre de la siguiente forma:

Te llamas: <nombre>

Tu edad es: <edad>

Eres: <sexo>
'''
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
sexo = input("Indica tu sexo:  (Recuerda: M para masculino o F para femenino)")
print(
    "Te llamas: {} \nTu edad es: {} \nEres: {}".format(nombre,edad,sexo)
)