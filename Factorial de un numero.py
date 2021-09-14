numero = int(input("Ingrese un numero entero positivo: "))
 
while numero < 0:
    print("El numero ingresado es incorrecto.")
    numero = int(input("Ingrese un numero entero positivo: "))
    
else:
    x = 1
    for i in range(2,numero + 1):
        x = x*i

    print("El factorial de",numero,"es:",x)