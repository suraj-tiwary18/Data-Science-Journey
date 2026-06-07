class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Roll No: {self.roll_no}, Name: {self.name}, Marks: {self.marks}")


class StudentManager:
    def __init__(self):
        self.students = []

    # Add Record
    def add_student(self):
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")

        student = Student(roll, name, marks)
        self.students.append(student)
        print("Student Added Successfully!")

    # View Records
    def view_students(self):
        if not self.students:
            print("No Records Found!")
        else:
            for student in self.students:
                student.display()

    # Search Record
    def search_student(self):
        roll = input("Enter Roll No to Search: ")

        for student in self.students:
            if student.roll_no == roll:
                student.display()
                return

        print("Student Not Found!")

    # Update Record
    def update_student(self):
        roll = input("Enter Roll No to Update: ")

        for student in self.students:
            if student.roll_no == roll:
                student.name = input("Enter New Name: ")
                student.marks = input("Enter New Marks: ")
                print("Record Updated Successfully!")
                return

        print("Student Not Found!")

    # Delete Record
    def delete_student(self):
        roll = input("Enter Roll No to Delete: ")

        for student in self.students:
            if student.roll_no == roll:
                self.students.remove(student)
                print("Record Deleted Successfully!")
                return

        print("Student Not Found!")


manager = StudentManager()

while True:
    print("\n===== Student Data Manager =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        manager.add_student()
    elif choice == "2":
        manager.view_students()
    elif choice == "3":
        manager.search_student()
    elif choice == "4":
        manager.update_student()
    elif choice == "5":
        manager.delete_student()
    elif choice == "6":
        print("Program Ended")
        break
    else:
        print("Invalid Choice!")