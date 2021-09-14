#Un programa que reciba un número entero y devuelva el numero en binario

numero = int(input("Dime un numero entero mayor o igual que cero: "))
binarios = []

if numero == 0:
    print("0 en binario es: 0")

elif numero < 0:
    print("Introduzca un numero entero mayor o igual que cero!")

else:
    print(numero,"en binario es:",end = " ")
    
    while numero != 0:
        residuo = numero%2
        binarios.insert(0,residuo)
        numero = numero//2

for x in binarios:
    print(x, end = "")
