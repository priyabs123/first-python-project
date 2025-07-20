def add_student():
    name = input("Enter student name: ")
    marks = float(input("Enter marks (out of 100): "))

    grade = calculate_grade(marks)

    with open("grades.txt", "a") as file:
        file.write(f"{name},{marks},{grade}\n")

    print(f"Student {name} added with grade {grade}.")

def calculate_grade(marks):
    if marks >= 90:
        return 'A+'
    elif marks >= 80:
        return 'A'
    elif marks >= 70:
        return 'B'
    elif marks >= 60:
        return 'C'
    elif marks >= 50:
        return 'D'
    else:
        return 'F'

def view_all_students():
    try:
        with open("grades.txt", "r") as file:
            lines = file.readlines()
            print("\nStudent Records:")
            for line in lines:
                name, marks, grade = line.strip().split(",")
                print(f"Name: {name}, Marks: {marks}, Grade: {grade}")
    except FileNotFoundError:
        print("No records found. Add students first.")

def main():
    while True:
        print("\nStudent Grade Management System")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_all_students()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()