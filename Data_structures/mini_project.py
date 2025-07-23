# Mini project using data structures

students = []

for i in range(3):
    name = input(f"Enter name of student {i+1}: ")
    marks = int(input("Enter marks: "))
    students.append({"name": name, "marks": marks})

print("Student Records:")
for student in students:
    print(student)
