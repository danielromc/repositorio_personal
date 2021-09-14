print("DIVISOR DE NÚMEROS")

dividendo = float(input("Escriba el dividendo: "))
divisor = float(input("Escriba el divisor: "))

if divisor == 0:
    print("La división por cero no está definida!")

else:
    cociente = dividendo / divisor
    resto = dividendo % divisor
    
    if dividendo % divisor == 0:
        print("La división es exacta. Cociente =", dividendo / divisor)
    
    else:
        print("La división no es exacta. Cociente =", cociente)
        
input("Presione ENTER para finalizar")
