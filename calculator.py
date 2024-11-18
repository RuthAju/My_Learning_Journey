def add(x, y):
    z = x + y
    return z


def subtract(x, y):
    
    z = x - y
    return z


def multiply(x, y):
    
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
}

def calculator():
    # User_input    
    x = int(input("Enter value for x: "))
    y = int(input("Enter value for y: "))
    operation = input("Enter an operation(+, -, *, /): ")

    if operation in operations:
        Answer = operations[operation](x, y)

    # Print answer
        print(f"{x} {operation} {y} = {Answer}")
        # print(Answer)
    else:
        print("Invalid operation!")  

        
calculator()