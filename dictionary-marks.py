students = {"Aashka": 90, "Aaryan": 85, "Ishita": 92, "Kunal": 88}
name = input("Enter student name: ")
if name in students:
    print("Marks:", students[name])
else:
    print("Student not found")
