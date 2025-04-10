import math_utils

def main():
    try:
        x = float(input("First number: "))
        y = float(input("Second number: "))
        operator = input("Operator (+, -, , /, *, %): ")

        operations = {
            '-': math_utils.subtract,
            '/': math_utils.divide,
            '+': math_utils.add,
            '**': math_utils.power,
            '*': math_utils.multiply,
            '%': math_utils.mod,
        }

        if operator in operations:
            result = operations[operator](x, y)
            print("Result:", result)
        else:
            print("Invalid operator")

    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
