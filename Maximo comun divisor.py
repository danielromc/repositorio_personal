def maxcd(a,b):
    lista1 = []
    lista2 = []
    lista3 = []
    
    #Divisores de a
    for i in range(1,abs(a) + 1):
        if a % i == 0:
            lista1.append(i)
    
    #Divisores de b
    for i in range(1,abs(b) + 1):
        if b % i == 0:
            lista2.append(i)
    
    #Divisores comunes de a y b
    for x in lista1:
        if x in lista2:
            lista3.append(x)
    
    #Maximo comun divisor
    mcd = max(lista3)
    print("El maximo conmun divisor de",a,"y",b,"es:",mcd)


