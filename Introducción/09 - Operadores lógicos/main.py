"""
Operadores lógicos regresan solo un valor
booleano (True/False)

	  ==, >, >=, <, <=, !=
	     and, or, not

"""

num_one = 10
num_two = 20

result = True and True #retorna True
print(result)
result = True and True and num_one == num_two #retorna False
print(result)
result = True and True or num_one == num_two #retorna True
print(result)

#Otra forma de escribir en orden las condiciones...
result = {
	True
	and num_one != num_two #True
	and num_one < 100 #True
	or num_two > 10 #False
}

print(result)

result = not True #False
print("not True:",result)

result = not not True #True
print("not not True:",result)


result = {
	(num_one == num_two or True) #False
	and (num_one < 100) #True
	and (num_two < 100) #True
	or (num_one > 100 and num_two > 200) #False
}
print(result)
