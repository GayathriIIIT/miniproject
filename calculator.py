import math

def square_root(x):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number")
    return math.sqrt(x)

def factorial(x):
    if x < 0:
        raise ValueError("Cannot compute factorial of a negative number")
    return math.factorial(x)

def natural_log(x):
    if x <= 0:
        raise ValueError("Cannot compute logarithm of zero or negative numbers")
    return math.log(x)

def power(x, b):
    return math.pow(x, b)

if __name__ == "__main__":
    while True:
        print("\nScientific Calculator Menu:")
        print("1. Square Root (√x)")
        print("2. Factorial (x!)")
        print("3. Natural Logarithm (ln(x))")
        print("4. Power Function (x^b)")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            num = float(input("Enter number: "))
            print("Result:", square_root(num))
        elif choice == "2":
            num = int(input("Enter number: "))
            print("Result:", factorial(num))
        elif choice == "3":
            num = float(input("Enter number: "))
            print("Result:", natural_log(num))
        elif choice == "4":
            x = float(input("Enter base (x): "))
            b = float(input("Enter exponent (b): "))
            print("Result:", power(x, b))
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")

