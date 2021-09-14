print("ÍNDICE DE MASA CORPORAL")

peso = float(input("Dime tu peso en kilogramos: "))
estatura0 = float(input("Dime tu estatura en centímetros: "))
estatura = estatura0/100

imc = peso/(estatura**2)

if imc <=18.5:
    print("Delgadez o bajo peso. Su IMC es:",imc)

elif 18.5 < imc < 25:
    print("Peso saludable. Su IMC es:",imc)

elif 25 <= imc <= 29.9:
    print("Sobrepeso. Su IMC es:",imc)

elif imc > 30:
    print("Obesidad. Su IMC es:",imc)
