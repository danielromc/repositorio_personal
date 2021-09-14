# Escriba un programa que pida dos números y que conteste cuál es el menor 
# y cuál el mayor o que escriba que son iguales.

print("COMPARADOR DE NÚMEROS")

primer_numero = float(input("Escriba un número: "))
segundo_numero = float(input("Escriba otro número: "))

if primer_numero > segundo_numero:
    print("El número menor es:",segundo_numero,"\nEl número mayor es:",primer_numero)
    
elif segundo_numero > primer_numero:
    print("El número menor es:",primer_numero,"\nEl número mayor es:",segundo_numero)
else:
    print("Los dos números son iguales.")
    
input("Presione ENTER para finalizar")