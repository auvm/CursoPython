nada = None
cadena = "Hola mundo"
cadena = "Adiós mundo"
entero = 42
flotante = 3.14
booleano = True
booleano = False
lista = [1, 2, 3, 4, 5]
listaCadena = ["Hola", "Mundo"]
listaMixta = [1, "Hola", 3.14, True, ("No", "Cambia")]
tuplaNoCambia = ("Master", "en", "Python")
diccionario = {
    "nombre":"Victor",
    "apellido":"Robles",
    "curso":"Python"
}
rango = range(0, 10)
dato_byte = b"Probando"

#imprimir variable
print(dato_byte)

#mostrar tipo de dato
print(type(dato_byte))

print("\n--------------------------\n")
#convertir un tipo de dato a otro
texto = "Hola, soy un texto"
numerito = str(100)
print(numerito, type(numerito))

#si no se convierte a texto, se produce un error
#ya que no se pueden concatenar un texto con un número
print(texto + " " + numerito)

numerito = int(100)
print(numerito, type(numerito))

numerito = float(100)
print(numerito, type(numerito))

