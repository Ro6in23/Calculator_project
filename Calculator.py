def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations ={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    continue_calc = True
    num1 = float(input("Enter your first_number: "))
    while continue_calc:
        for symbol in operations:
            print(symbol)
        user_input = input("Pick an operation: ")
        num2 = float(input("Enter your next_number: "))
        result = operations[user_input](num1,num2)
        print(f"{num1} {user_input} {num2} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

        if choice == "y":
            num1=result
        else:
            continue_calc = False
            print("\n"*20)
            calculator()


calculator()
