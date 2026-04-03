# Student Management System

students = []

while True:
    print("\n--- MENU ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Marks")
    print("4. Remove Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # 1️⃣ Add Student
    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        marks = int(input("Enter marks: "))

        student = {
            "name": name,
            "age": age,
            "marks": marks
        }

        students.append(student)
        print("Student added successfully!")

    # 2️⃣ View Students
    elif choice == "2":
        if len(students) == 0:
            print("No students found!")
        else:
            for i, s in enumerate(students):
                print(f"{i+1}. {s['name']} - Age: {s['age']} - Marks: {s['marks']}")

    # 3️⃣ Update Marks
    elif choice == "3":
        name = input("Enter student name to update: ")

        for s in students:
            if s["name"] == name:
                new_marks = int(input("Enter new marks: "))
                s["marks"] = new_marks
                print("Marks updated!")
                break
        else:
            print("Student not found!")

    # 4️⃣ Remove Student
    elif choice == "4":
        name = input("Enter student name to remove: ")

        for s in students:
            if s["name"] == name:
                students.remove(s)
                print("Student removed!")
                break
        else:
            print("Student not found!")

    # 5️⃣ Exit
    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")