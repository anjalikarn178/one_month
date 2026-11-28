
students = {}


def add_student():
    roll = input("Enter roll number: ")

    if roll in students:
        print("Student already exists!")
        return

    name = input("Enter student name: ")
    branch = input("Enter branch: ")

    try:
        marks = float(input("Enter marks: "))
        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return
    except ValueError:
        print("Enter valid numeric marks.")
        return

    students[roll] = {
        "name": name,
        "branch": branch,
        "marks": marks
    }

    print("Student added successfully!")


def display_students():
    if not students:
        print("No student records found.")
        return

    for roll, details in students.items():
        print(
            f"Roll: {roll} | "
            f"Name: {details['name']} | "
            f"Branch: {details['branch']} | "
            f"Marks: {details['marks']}"
        )


def search_student():
    roll = input("Enter roll number to search: ")

    if roll in students:
        print(students[roll])
    else:
        print("Student not found!")


def update_marks():
    roll = input("Enter roll number: ")

    if roll not in students:
        print("Student not found!")
        return

    try:
        marks = float(input("Enter new marks: "))
        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return
    except ValueError:
        print("Invalid marks.")
        return

    students[roll]["marks"] = marks
    print("Marks updated successfully!")


def delete_student():
    roll = input("Enter roll number to delete: ")

    if roll in students:
        del students[roll]
        print("Student deleted!")
    else:
        print("Student not found!")


def calculate_average():
    if not students:
        print("No records available.")
        return

    total = sum(s["marks"] for s in students.values())
    average = total / len(students)

    print(f"Average marks: {average:.2f}")


def find_topper():
    if not students:
        print("No records available.")
        return

    topper = max(
        students.items(),
        key=lambda item: item[1]["marks"]
    )

    print("Topper:", topper[1]["name"])
    print("Marks:", topper[1]["marks"])


def students_above_80():
    found = False

    for roll, details in students.items():
        if details["marks"] > 80:
            print(roll, details)
            found = True

    if not found:
        print("No students scored above 80.")


def display_branches():
    branches = {s["branch"] for s in students.values()}
    print("Unique branches:", branches)


def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Calculate Average")
        print("7. Find Topper")
        print("8. Students Above 80")
        print("9. Display Unique Branches")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_marks()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            calculate_average()
        elif choice == "7":
            find_topper()
        elif choice == "8":
            students_above_80()
        elif choice == "9":
            display_branches()
        elif choice == "10":
            print("Exiting application.")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
