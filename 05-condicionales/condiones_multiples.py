import os
os.system("clear")
print("************** EJEMPLO 5  *****************")

edad_minima = 18
edad_maxima = 65
# edad = int(input("¿Cuántos años tienes?: "))
edad = 20

if edad >= edad_minima and edad <= edad_maxima:
    print("Está en edad de trabajar")
else:
    print("No está en edad de trabajar")

#operadores lógiccos: and, or, not

print("************** EJEMPLO 6  *****************")

pais = "Alemania"

if pais == "México" or pais == "España" or pais == "Colombia":
    print("Eres de un país de habla hispana")
else:
    print("No eres de un país de habla hispana")



print("************** EJEMPLO 7  *****************")

pais = "México"

if not (pais == "México" or pais == "España" or pais == "Colombia"):
    print("No eres de un país de habla hispana")
else:
    print("Eres de un país de habla hispana")

print("************** EJEMPLO 8  *****************")

pais = "USA"
if pais != "México" and pais != "España" and pais != "Colombia":
    print(f"{pais} no es un país de habla hispana")
else:   
    print(f"{pais} es un país de habla hispana")
