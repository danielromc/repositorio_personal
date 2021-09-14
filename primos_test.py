a = int(input("Ingrese un numero entero: "))
count = 0

if a == 1:
    print("El 1 no es ni primo ni compuesto")

elif a>1:
      
    for i in range(2,a):
        resto = a%i
        if resto == 0:
            count = count + 1
            
    if count >= 1:
        print("El",a,"es un número compuesto")
    else:
        print("El",a,"es un número primo")

else:
    print("El numero ingresado es incorrecto. Intente nuevamente.")
