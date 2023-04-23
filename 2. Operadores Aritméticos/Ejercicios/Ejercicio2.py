'''Enunciado:
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete, 
así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
Cada payaso pesa 112 g y cada muñeca 75 g. Un cliente frecuente pide la cantidad de 23 payasos y 54 muñecas, 
realiza un programa que muestre el peso total de toda la venta.
'''
# 1@ Forma de resolverlo con variables detalladas
peso_payaso = 112
peso_muñeca = 75
pedi_payaso = 23
pedi_muñec = 54
# Calculamos el peso total de los payasos y las muñécas, y posteriormente realizamos la suma de ambas operaciones.
PesoPedido = (peso_payaso * pedi_payaso) + (peso_muñeca * pedi_muñec)
#print(PesoPedido) 

# 2@ Forma de resolverlo con una sola variable
PesoPedido = ((112 * 23) + (75 * 54))
#print(PesoPedido)

# 3@ Forma de resolverlo sin variables
#print((112*23)+(75*54))

# El resultado es 6626 gramos
print("El peso total del pedido es: ", PesoPedido, "gramos")