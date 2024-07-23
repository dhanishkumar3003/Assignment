def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def calculator():
    print("Enter two numbers:")
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))
    
    print("\nChoose an operation:")
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    
    choice = int(input("Enter your choice : "))
    
    if choice == 1:
        result = add(num1, num2)
    elif choice == 2:
        result = subtract(num1, num2)
    elif choice == 3:
        result = multiply(num1, num2)
    elif choice == 4:
        result = divide(num1, num2)
    else:
        result = "Invalid choice!"
    
    print(f"The result is: {result}")

if __name__ == "__main__":
    calculator()
