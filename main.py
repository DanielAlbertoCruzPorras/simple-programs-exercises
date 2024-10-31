C1 = float(input("Digit your first note: "))
C2 = float(input("Digit your second note: "))
Nl = float(input("Digit you laboratory note: "))
Nc = (60 - Nl*0.3)/0.7
C3 = (3 * Nc) - (C1 + C2)
print(f"You need a {C3:.2f} on the tird note")
