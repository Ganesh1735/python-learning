print("1.Add Student")
print("2.View Student")

choice = input("Enter your choice:")

students = []
if choice =="1":
    name=input("Enter student name:")

    if name:
        students.append(name)
        print("Student added!")

    else:
        print("Please enter a student name.")

    with open("students0.txt","a") as file:
        for student in students:
            file.write(student+"\n")

    print("Students saved successfully!")   



elif choice == "2":
    print("All Students:")
else:
    print("Invalid choice!")
    with open ("students0.txt","r") as file:
        for student in file:
            print(student.strip())



    

        
