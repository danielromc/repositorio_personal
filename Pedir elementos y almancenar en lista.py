familia = []
names = ""

while True:
    names = input("Dime los nombres de tus familiares: ")
    if names == "0":
        break
    else:
        familia.append(names)

print(familia)