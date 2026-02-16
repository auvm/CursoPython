"""
una variebl es un contenedor de información
que dentro guardará un dato, se pueden crear 
varias variables y que cada uno tenga un dato distinto.
"""

texto = "Master en python"
texto2 = texto.upper()
numero = 45
decimal = 3.14
booleano = True

print(texto)
print(texto2)
print(numero)
print(decimal)
print(booleano)

print("-----------------------------")

# concatenación

nombre = "Victor"
apellido = "Robles"
web = "victorroblesweb.es"
print(nombre + " " + apellido + " - " + web)
print(f"{nombre} {apellido} - {web}")
print("Hola me llamo {} {} y mi web es: {}".format(nombre, apellido, web))

print(nombre, apellido, web)