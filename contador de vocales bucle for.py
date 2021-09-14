frase = input("Ingrese una frase: ")

contador = 0

for i in frase:
    if i in "aeiou":
        contador = contador + 1
print(contador)

