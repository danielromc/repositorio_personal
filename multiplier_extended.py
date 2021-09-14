number = int(input("Enter a whole number: "))
maximus = int(input("How many multiples you want to print?: "))

for element in range(1, maximus+1):
    multiple = number*element
    print(multiple)
