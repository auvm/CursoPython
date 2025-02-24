#	    0	    1      2	     3		 4		5
lista = ["python", "c", "flask", "mongo db", "maria db", "javascript"]
print(lista)

#así se puede acceder a cada elemento
value01 = lista[0]
value02 = lista[1]
value03 = lista[2]

#así se obtiene el número total de elementos en la lista
num_elements = len(lista)

print("número de elementos guardados: ",num_elements)


"""
Para acceder al último elemento de la lista, sin saber
su índice, se puede utilizar en número total de elementos
menos -1 (ya que los indices empiezan desde 0). 
"""

print(lista[len(lista)-1])


"""
La forma en que se pueden ver los índices es que son una lectura
de izquierda a derecha (->) de los elementos de la lista.

Pero hay otra forma de lectura pythonica que es leer de
derecha a izquierda (<-) y eso se hace con números negativos.

	   -6	   -5     -4	    -3		-2	       -1
lista = ["python", "c", "flask", "mongo db", "maria db", "javascript"]

"""

print("primer elemento: ",lista[-6])
print("último elemento: ",lista[-1])


#indices fuera del número real de elementos en la lista provoca un error
#print(lista[99])



"""
mediante la re-asignación de elementos con ayuda de su 
índice, se pueden actualizar sus valores.
"""
lista[0] = "pizza"
lista[1] = "papas"
lista[2] = "hot dogs"
lista[3] = "banderillas"

print(lista)
