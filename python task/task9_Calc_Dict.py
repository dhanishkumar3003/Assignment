def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

operations = {
    1: add,
    2: subtract,
    3: multiply,
    4: divide
}

def calculator():
    while True:
        print("\nOptions:")
        print("1) Addition")
        print("2) Subtraction")
        print("3) Multiplication")
        print("4) Division")
        print("5) Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice in operations:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            result = operations[choice](x,y)
            print(f"Result: {result}")
        else:
            exit(0)

if __name__ == "__main__":
    calculator()
