def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero"

def power(x, y):
    return x ** y

def mod(x, y):
    try:
        return x % y
    except ZeroDivisionError:
        return "Error: Division by zero"

if __name__ == "__main__":
    print("     Test    ")
    print(f"add(8, 2) = {add(8, 2)}")
    print(f"subtract(4, 5) = {subtract(4, 5)}")
    print(f"multiply(9, 2) = {multiply(9, 2)}")
    print(f"divide(4, 0) = {divide(4, 0)}")
    print(f"divide(88, 1) = {divide(88, 1)}")
    print(f"power(2, 3) = {power(2, 3)}")
    print(f"mod(77, 2) = {mod(77, 2)}")
