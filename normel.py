# Simple Python Program

def greet(name):
    return f"Hello, {name}! Welcome to Python programming."

def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    result = add_numbers(num1, num2)
    print("The sum is:", result)