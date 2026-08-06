students = []
def add_student():
    name = input("Enter student name:")
    students.append(name)
    print("Student added successfully!")

def view_students():
    print("\nStudent List:")
    print(students)

def delete_student():
    name = input("Enter student name to delete:")

    if name in students:
        students.remove(name)
        print("Student deleted successfully!")
    else:
        print("Student not found!")

def search_student():
    name = input("Enter student name to search:")

    if name in students:
        print("Student Found!")
    else:
        print("Student not found!")

while True:
    print("\n==== Student Management System ====")
    print("1.Add Student")
    print("2.view Students")
    print("3.Delete Student")
    print("4.Search Student")
    print("5.Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        delete_student()

    elif choice == "4":
        search_student()
    
    elif choice == "5":
        print("Thank you!")
        break
            
    else:
        print("Invalid choice")
