num1 = 40
num2 = 99.99

print(type(num1))
print(num1)

float(num1) # Aunque 40 sea un número entero, con la función float, lo transformamos en decimal. (Sólo obtiene la parte decimal)

print(float(num1)) # Aquí se muestra como cambia el número de entero a decimal.

int(num2) # Aunque 99.99 sea un número decimal, con la funcion int, lo transformamos en entero. (No lo redondea, solo obtiene la parte entera)

print(type(int(num2)))