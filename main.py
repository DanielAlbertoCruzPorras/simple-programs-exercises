num1 = float(input("Insert a number: "))
num2 = float(input("Insert a number: "))

if num1>num2:
    print(f"{num2} {num1}")
else:
    print(f"{num1} {num2}")

num1 = float(input("Insert a number: "))
num2 = float(input("Insert a number: "))
num3 = float(input("Insert a number: "))
numeros = [num1, num2, num3]
numeros.sort()

print(*numeros) #Imprime sin corchetes ni comas (Recuerde que es una tupla)
 
#Ordenar cuatro números flotantes
num1 = float(input("Insert a number: "))
num2 = float(input("Insert a number: "))
num3 = float(input("Insert a number: "))
num4 = float(input("Insert a number: "))

numeros = [num1, num2, num3, num4]
numeros.sort()

print(*numeros)



