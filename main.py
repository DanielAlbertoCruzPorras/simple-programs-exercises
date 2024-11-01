# Get the lengths of the triangle's sides
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

# Check if the sides satisfy the triangle inequality
if (a + b > c) and (a + c > b) and (b + c > a):
    # Determine the type of triangle
    if a == b == c:
        print("The triangle is equilateral.")
    elif a == b or b == c or a == c:
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")
else:
    print("It is not a valid triangle.")

