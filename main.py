b = 1
while b == 1:
    num = float(input("Inserte un número par mayor a 10: "))
    if num > 10:
        if num % 2 == 0:
            b = 0
        else:
            print("El número es mayor que 10 pero es impar o fraccionario, inserte otro número que cumpla las condiciones")
    else:
        print("El número es menor a 10, inserte otro que cumpla las condiciones")
