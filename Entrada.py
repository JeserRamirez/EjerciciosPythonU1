#Entrada de datos: 
print ("ingresa tu numbre")
nombre = input()
print(type(nombre))

palabras = nombre.split(" ")

nombre = nombre.capitalize()

capitalizado = [p.capitalize() for p in nombre.split()]
concatenar = ' '.join(capitalizado)

print(concatenar)