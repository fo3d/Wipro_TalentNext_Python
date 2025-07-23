# Mini project with exception handling

def get_integer_input(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("That was not a number.")
        return None

distance = None
while distance is None:
    distance = get_integer_input("Enter distance in miles: ")

if distance < 3:
    print("Use Bicycle")
elif distance < 300:
    print("Use Motor-cycle")
else:
    print("Use Super-Car")
