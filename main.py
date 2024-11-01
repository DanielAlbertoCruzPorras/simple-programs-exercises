operand1 = float(input("Enter operand: "))
operator = input("Enter operator (+, -, *, /): ")
operand2 = float(input("Enter operand: "))

if operator == '+':
    result = operand1 + operand2
    print(f"{operand1} + {operand2} = {result}")
elif operator == '-':
    result = operand1 - operand2
    print(f"{operand1} - {operand2} = {result}")
elif operator == '*':
    result = operand1 * operand2
    print(f"{operand1} * {operand2} = {result}")
elif operator == '/':
    if operand2 != 0:
        result = operand1 / operand2
        print(f"{operand1} / {operand2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operator.")

