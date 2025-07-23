# Command Line Argument Mini Project
import sys

if len(sys.argv) != 2:
    print("Usage: python mini_project.py <distance>")
else:
    distance = int(sys.argv[1])
    if distance < 3:
        print("Bicycle")
    elif distance < 300:
        print("Motor-cycle")
    else:
        print("Super-Car")
