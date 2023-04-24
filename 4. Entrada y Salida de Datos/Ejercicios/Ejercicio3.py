'''Enunciado:
Escribir un programa que solicite al usuario una vocal en minuscula, y luego una letra en mayúsculas. El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas
'''
vocal = input("Escribe una vocal en MINÚSCULA: ")
consonante = input("Escribe una consonante en MAYÚSCULA: ")

vocal = vocal.upper() # Transformamos la vocal introducida por el usuario en MAYUS
consonante = consonante.lower() # Transformamos la consonante introducida por el usuario en MINUS
print("La consonante fue: {}\nLa vocal fue: {}".format(consonante,vocal))