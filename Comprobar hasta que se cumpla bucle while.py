"""Ejemplo de un bucle while para pedir numeros por teclado hasta que se
inserte el correcto"""

comprobar = True

while comprobar == True:
    n = int(input("Ingrese un numero entero positivo: "))
    
    if n > 0:
    
        for i in range(5):
            print(n,"multiplicado por",i,"es igual a",n*i)
            
        comprobar = False

    else:
        print("El numero ingresado es incorrecto. Intente nuevamente.")
    

