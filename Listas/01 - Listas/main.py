"""
Estructura de datos que permite almacenar
otros tipos de datos, como entereos, cadenas,
flotates, booleanos u otras listas.

Se denotan por [ ]
"""

lista = ["cadena", 10, 99.99, True, False, [1, 2, 3, 4]]

print(lista, " - ", type(lista))


"""
La buena practica es que las listas SOLO contengan
elementos de un SOLO tipo de dato.
"""

courses = ["flash", "ruby", "mongo db", "c++"]
numbers = [1, 2, 3, 4, 5, 6]

print(courses, " - ", type(lista))
print(numbers, " - ", type(lista))


"""
Se accede a los elementos de una lista mediante ÍNDICES,
que comienza desde el 0 (cero).
"""
print(courses[0])
