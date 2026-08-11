import json
import os

FILE_NAME = "students.json"

def load_students():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

def add_student():
    students = load_students()

    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    save_students(students)

    print("Student added successfully!")

def view_students():
    students = load_students()

    if not students:
        print("No student records found.")
        return

    print("\n--- Student Records ---")

    for student in students:
        print(f"ID     : {student['id']}")
        print(f"Name   : {student['name']}")
        print(f"Age    : {student['age']}")
        print(f"Course : {student['course']}")
        print("------------------------")

def update_student():
    students = load_students()

    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student["id"] == student_id:
            print("Leave a field blank to keep the old value.")

            name = input(f"Enter Name [{student['name']}]: ")
            age = input(f"Enter Age [{student['age']}]: ")
            course = input(f"Enter Course [{student['course']}]: ")

            if name:
                student["name"] = name
            if age:
                student["age"] = age
            if course:
                student["course"] = course

            save_students(students)
            print("Student updated successfully!")
            return

    print("Student not found!")

def delete_student():
    students = load_students()

    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students(students)

            print("Student deleted successfully!")
            return

    print("Student not found!")

def main():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            update_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            print("Program ended.")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
