# Jerarquía de operaciones
num1 = 100
num2 = 50
num3 = 25
num4 = 10

# Por defecto primero realiza la multiplicación
print(num1 + num2 * num3) # Da un resultado de 1350
# Queremos que primero se realice la suma, por lo que usamos paréntesis
print((num1 + num2) * num3) # Da un resultado de 3750
# Primero se realiza el parentesis [La suma], luego la multiplicación y luego la resta.
print((num1 + num2) * num3 - num4) # Da un resultado de 3740
# Pero queremos que antes de hacer la multiplicación queremos que se realice la resta.
print((num1 + num2) * (num3 - num4)) # Da un resultado de 2250