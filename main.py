dividend = float(input("Insert the dividend: "))
divisor = float(input("Insert the divisor: "))
div = dividend/divisor
quot = div - (div % 1)
rest = (div % 1)* divisor
if div % 1 == 0:
    print(f"the division is exact\nQuotient: {quot:.0f}\nRest: {rest:.0f}")
else:
    print(f"the division is not exact\nQuotient: {quot:.0f}\nRest: {rest:.0f}")
