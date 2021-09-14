#Un programa que le pide al usuario los tres lados de un triángulo y determina si
#el triángulo es equilátero, isosceles o escaleno.

primer_lado = float(input("Longitud del primer lado: "))
segundo_lado = float(input("Longitud del segundo lado: "))
tercer_lado = float(input("Longitud del tercer lado: "))

if primer_lado == segundo_lado == tercer_lado:
    print("El triángulo es equilátero")
    
elif primer_lado == segundo_lado or primer_lado == tercer_lado or segundo_lado == tercer_lado:
    print("El triángulo es isosceles")
    
else:
    print("El triángulo es escaleno")