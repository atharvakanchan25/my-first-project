import os

class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.roll},{self.name},{self.marks}"

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    student = Student(roll, name, marks)
    with open("students.txt", "a") as file:
        file.write(str(student) + "\n")
    print(" Student added successfully!\n")

def view_students():
    print("\n--- Student List ---")
    if not os.path.exists("students.txt"):
        print("No student records found.")
        return
    with open("students.txt", "r") as file:
        for line in file:
            roll, name, marks = line.strip().split(",")
            print(f"Roll: {roll}, Name: {name}, Marks: {marks}")
    print()

def search_student():
    roll = input("Enter Roll Number to search: ")
    found = False
    with open("students.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == roll:
                print(f"Found: Roll: {data[0]}, Name: {data[1]}, Marks: {data[2]}")
                found = True
                break
    if not found:
        print("Student not found.\n")

def update_student():
    roll = input("Enter Roll Number to update: ")
    students = []
    found = False

    with open("students.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == roll:
                name = input("Enter New Name: ")
                marks = input("Enter New Marks: ")
                students.append(Student(roll, name, marks))
                found = True
            else:
                students.append(Student(*data))

    with open("students.txt", "w") as file:
        for student in students:
            file.write(str(student) + "\n")

    if found:
        print("Student updated successfully!\n")
    else:
        print("Student not found.\n")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    students = []
    found = False

    with open("students.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] != roll:
                students.append(Student(*data))
            else:
                found = True

    with open("students.txt", "w") as file:
        for student in students:
            file.write(str(student) + "\n")

    if found:
        print(" Student deleted successfully!\n")
    else:
        print(" Student not found.\n")

# Main Menu
while True:
    print("====== Student Management System ======")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print("👋 Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")
