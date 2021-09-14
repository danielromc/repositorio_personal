number = int(input("Dime un numero entero: "))

if number > 0:
    for i in range(1,number + 1):
        if number%i == 0:
            print("El numero",i,"es divisor de",number)
               
elif number < 0:
    for i in range(number,0):
        if number%i == 0:
            print("El numero",i,"es divisor de",number)
    

else:
    print("El cero tiene infinitos divisores, salvo el 0.")