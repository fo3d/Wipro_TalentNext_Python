# Exception handling example

try:
    num = int(input("Enter a number: "))
    print("100 /", num, "=", 100 / num)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input.")
