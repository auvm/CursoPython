#strings

"""
Dentro de una cadena encerrada entre comillas dobles " ", 
puede haber comillas simples ' '. Y viceversa, si se usan
comillas simples, se pueden usar dentro comillas dobles.
"""
first_name = "código";
last_name = 'facilito';

print(first_name,": ", type(first_name));
print(last_name,": ", type(last_name));


#integers

age = 13;
print(age, ": ", type(age));

"""
si trabajamos con números grandes, podemos segmentar
en lugar de comas, podemos usar guiones bajos.
"""

number = 10_000_000; #diez millones
print(number, ": ", type(number));

#floats
"""
Igual que con los enteros, pero podremos usar puntos
decimales con o sin signo
"""

number = 100_000.99;
print(number, ": ", type(number));


#booleans
"""
Para valores True / False
"""

is_active = False;
print(is_active, ": ",type(is_active));
is_active = True;
print(is_active, ": ",type(is_active));

