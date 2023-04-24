# Métodos Booleanos
cadena = "Estoy mostrando los métodos booleanos para las Strings"
cadena2 = "CMSALKA"
cadena3 = "holayadios"
# Si empieza con...
print(cadena.startswith("E")) # Devuelve True
print(cadena.startswith("e")) # Devuelve False
# Si termina con...
print(cadena.endswith("s")) # Devuelve True
print(cadena.endswith("S")) # Devuelve False
# Si todo el contenido de la cadena está en MAYUS
print(cadena.isupper()) # Devuelve False
print(cadena2.isupper()) # Devuelve True
# Si todo el contenido de la cadena está en MINUS
print(cadena3.islower()) # Devuelve True
print(cadena.islower()) # Devuelve False