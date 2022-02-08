from art import logo

print(logo)


# write calculate function

def add(a, b):
    return a + b

def subtract(a, b):
    return a -b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# dictionary for function

cal = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

Continue = True

while Continue:
    FirstNumber = int(input("Input your first number: "))
    SecondNumber = int(input("Input your second number: "))
    Operation = input("what is your operation? ")
    Result = cal[Operation](FirstNumber, SecondNumber)
    print(Result)
    Condition = input("Would you like to have another operation?")
    if Condition == "yes":
        Continue = True
    else:
        Continue = False



