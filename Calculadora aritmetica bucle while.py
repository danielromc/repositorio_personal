"""Calculadora aritmética. Tiene un menú en el que se debe seleccionar una operación
y posteriormente dos número para aplicar dicha operación """


print("Calculadora aritmética")
print("1 para Sumar")
print("2 para Restar")
print("3 para multiplicar")
print("4 para Dividir")
print("5 para Salir")
operador = input("Ingrese la operación: ")


while True:
    
    if operador == "1":
        sumando1 = float(input("Ingrese el primer sumando: "))
        sumando2 = float(input("Ingrese el segundo sumando: "))
        print("El resultado de la suma es:",sumando1 + sumando2)
        
    elif operador == "2":
        minuendo = float(input("Ingrese el minuendo: "))
        sustraendo = float(input("Ingrese el sustraendo: "))
        print("El resultado de la resta es:",minuendo - sustraendo)
        
    elif operador == "3":
        factor1 = float(input("Ingrese el primer factor: "))
        factor2 = float(input("Ingrese el segundo factor: "))
        print("El resultado de la multiplicación es:",factor1*factor2)
    
    elif operador == "4":
        dividendo = float(input("Ingrese el dividendo: "))
        divisor = float(input("Ingrese el divisor"))
        if divisor == 0:
            print("La division por cero no está definida")
        else:
            print("El resultado de la division es:",dividendo/divisor)
            
    elif operador == "5":
        break
        
    print()
    print("1 para Sumar")
    print("2 para Restar")
    print("3 para multiplicar")
    print("4 para Dividir")
    print("5 para Salir")
    operador = input("Ingrese la operación: ")