year = int(input("Insert a year: "))
if year < 1582:
    if year % 4 == 0:
        print("That year is a leap year")
    else:
        print("That year is'nt a leap year")
elif year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("That year is a leap year")
        else:
            print("That year is'nt a leap year")
    else:
        print("That year is a leap year")
else:
    print("That year is'nt a leap year")
