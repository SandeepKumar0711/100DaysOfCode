import art_day10

def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

def calculator():
    print(art_day10.logo)
    calc_dict = {"+": add, "-": substract, "*": multiply, "/": divide}

    num1 = float(input("What's the first number?: "))
    for key in calc_dict:
        print(key)
    calc_cont='y'
    while calc_cont=='y':
        operator = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        answer = calc_dict[operator](num1, num2)
        print(f"{num1} {operator} {num2} = {answer}")
        num1=answer
        calc_cont=input(f"Type 'y' to continue calculating with {answer}, ot type 'n' to start a new calculation: ")
    calculator()

calculator()