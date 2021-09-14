number = int(input("Dime un número entero: "))

if number > 0:
    print("Los divisores de",number,"son:",end=" ")
    for i in range(1,number + 1):
        if number%i == 0:
            print(i,end=", ")
               

else:
    print("Debes introducir un número mayor que cero")