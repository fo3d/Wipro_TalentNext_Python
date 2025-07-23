# Mini project to log user input to a file

filename = "user_log.txt"

with open(filename, "a") as f:
    name = input("Enter your name: ")
    f.write(f"User entered: {name}\n")

print("Your name has been logged.")
