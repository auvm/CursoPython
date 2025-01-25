#int 
number = 100
result = number + 10
result = number - 10

print("El resultado es :", result)

#float
result = number / 10 #la división siempre genera un float
print("El resultado es :", result)

#int
result = number // 10 #el resultado con doble // genera solo el entero
		      #de la división.
print("El resultado es :", result)


#números negativos
result = number * -1
print("El resultado es :", result)
result = -10
print("El resultado es :", result)


#ayudas visuales
"""
Los números grandes pueden separarse, pero no con ( , ) coma,
sino con guines bajos ( _ ) en el código para que se vean
mejor y se puedan leer con facilidad. Sin ver afectado
el valor real e impreso al final.
Ejemplo:
"""
numero_grande = 10_000_000 #diez millones
print(f"${numero_grande}") #con print(f"{variable}") puedo imprimir variables dentro de un string
