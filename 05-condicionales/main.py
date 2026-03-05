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


print("************** EJEMPLO 3  *****************")

nombre = input("¿Cómo te llamas?: ")
ciudad = input("¿En qué ciudad vives?: ")
continente = input("¿En qué continente vives?: ")
edad = int(input("¿Cuántos años tienes?: "))
mayoria_edad = 18

if edad >= mayoria_edad:

    print(f"{nombre} es mayor de edad")

    if continente.lower() == "america":
        print("Eres de América")
    else:
       print("No eres de América")

else:
    print(f"{nombre} es menor de edad")