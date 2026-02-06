import json
import os

FILE_NAME = "students.json"


# ---------- Function to take student input ----------
def get_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    marks = int(input("Enter marks: "))

    return {
        "name": name,
        "age": age,
        "marks": marks
    }


# ---------- Function to save student ----------
def save_student(student):
    students = []

    # Read existing data if file exists
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            try:
                students = json.load(file)
            except json.JSONDecodeError:
                students = []

    students.append(student)

    # Write updated list back to file
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# ---------- Function to read students ----------
def read_students():
    if not os.path.exists(FILE_NAME):
        print("No student data found.")
        return

    with open(FILE_NAME, "r") as file:
        students = json.load(file)

        if not students:
            print("No students available.")
            return

        for index, student in enumerate(students, start=1):
            print(f"\nStudent {index}")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Marks:", student["marks"])


# ---------- Main Menu ----------
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student = get_student()
        save_student(student)
        print("✅ Student saved successfully!")

    elif choice == "2":
        read_students()

    elif choice == "3":
        print("👋 Exiting program. Bye!")
        break

    else:
        print("❌ Invalid choice. Try again.")


