# File read/write operations

with open("sample.txt", "w") as f:
    f.write("This is a sample file.")

with open("sample.txt", "r") as f:
    content = f.read()
    print("File Content:", content)
