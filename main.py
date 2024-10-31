a = int(input("Actual Hour: "))
b = int(input("Cuantity of time: "))
print(f"En {b:.0f} horas, el reloj marcará las {((a+b)%24):.0f}")