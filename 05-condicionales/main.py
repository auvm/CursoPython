"""
Condicional IF

SI se_cumple_x_condición:
    haz_algo
SI NO:
    haz_otra_cosa

if se_cumple_x_condición:
    haz_algo
elif se_cumple_y_condición:
    haz_otra_cosa
else:
    haz_otra_cosa_mas
"""

print("************** EJEMPLO 1 *****************")

#color = input("Adivina cuál es mi color favorito: ")
color = "rojo"
if color == "rojo": #igual igual, es pregunta, no asignación
    print("En horabuena!!!")
    print("El color es rojo")
else:
    print("Color incorrecto")

"""
== igual que
!= diferente que
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que
"""
print("************** EJEMPLO 2 *****************")

year = int(input("¿En qué año estamos?: "))
if year >= 2021:
    print("Estamos de 2021 en adelante")
else:
    print("Estamos antes de 2021")