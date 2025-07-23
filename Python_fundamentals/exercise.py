# Q1. Check if a number is Positive, Negative or Zero
def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

# Q2. Check if a number is Odd or Even
def check_odd_even(n):
    return "Even" if n % 2 == 0 else "Odd"
