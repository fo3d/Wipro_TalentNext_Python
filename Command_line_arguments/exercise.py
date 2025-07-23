# Command Line Argument Exercise
import sys

if len(sys.argv) > 1:
    print(f"Arguments received: {sys.argv[1:]}")
else:
    print("No command line arguments provided.")

