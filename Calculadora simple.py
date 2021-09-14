"""Ejemplo de calculadora de las cuatro operaciones básicas"""

primer_numero = float(input("Ingrese el primer número: "))
segundo_numero = float(input("Ingrese el segundo número: "))

print()
print("Escoja una operación aritmética según la siguiente información: ")
print("A para sumar")
print("B para restar")
print("C para multiplicar")
print("D para dividir")

operador_aritmetico = input("Opción a escoger: ")

if operador_aritmetico == "A" or operador_aritmetico == "a":
    print("El resultado es:",primer_numero+segundo_numero)

elif operador_aritmetico == "B" or operador_aritmetico == "b":
    print("El resultado es:",primer_numero-segundo_numero)

elif operador_aritmetico == "C" or operador_aritmetico == "c":
    print("El resultado es:",primer_numero*segundo_numero)

elif operador_aritmetico == "D" or operador_aritmetico == "d":
    if segundo_numero == 0:
        print("La división por cero no está definida.")
    else:
        print("El resultado es:",primer_numero/segundo_numero)

else:
    print("Operador incorrecto")