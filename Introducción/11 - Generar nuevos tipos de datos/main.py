"""
Si requerimos que el resultado de una entrada por teclado
sea de un tipo float, int o bool, debemos castearlos
con las siguientes funciones:
"""

first_name = input("Ingresa tu nombre: ") 	#retorna un str por default
age = int(input("Edad: "))			#retorna int
height = float(input("Altura: "))		#retora float	
status = input("¿Tu usuario está activo? s/n: ") == "s" #solo con una validación
							#se puede retornar bool
print(first_name, type(first_name))
print(age, type(age))
print(height, type(height))
print(status, type(status))


print("convierte int o float a string: ", str(196.84))  #int o float -> a string
