def calculator():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            break
        except ValueError:
            print("Please enter a number.")

    operand = ''
    while operand not in ['+', '-', '*', '/', '%']:
        operand = input("Enter operation (+, -, *, /, %): \n")
        if operand not in ['+', '-', '*', '/', '%']:
            print("Try again")

    while True:
        try:
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("Please enter a number.")

    if operand == '+':
        answer = num1 + num2
    elif operand == '-':
        answer = num1 - num2
    elif operand == '*':
        answer = num1 * num2
    elif operand == '/':
        if num2 == 0:
            print("Error: Division by zero")
            return
        else:
            answer = num1 / num2
    elif operand == '%':
        answer = num1 % num2

    print(f"{num1} {operand} {num2} = {answer}")

if __name__ == "__main__":
    while True:
        calculator()
        cont = input("EXIT? (y/n): ").lower()
        while cont not in ['y', 'n']:
            if cont == 'y':
                break
        if cont == 'y':
            print("| EXIT |")
            break

