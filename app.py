# Student Grade Management System

'''
Features:

* Add a new student with grades.
* View all students and their grades.
* Update a student's grades.
* Calculate the average grade for each student.
* Delete a student record.

'''

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def view_grades(self):
        return self.grades

    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

class GradeManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        if name in self.students:
            print("Student already exists.")
        else:
            self.students[name] = Student(name)
            print(f"Student {name} added successfully.")

    def add_grade(self, name, grade):
        if name in self.students:
            self.students[name].add_grade(grade)
            print(f"Grade {grade} added for student {name}.")
        else:
            print("Student does not exist.")

    def view_student(self, name):
        if name in self.students:
            grades = self.students[name].view_grades()
            print(f"Grades for {name}: {grades}")
        else:
            print("Student does not exist.")

    def update_grade(self, name, old_grade, new_grade):
        if name in self.students:
            if old_grade in self.students[name].grades:
                index = self.students[name].grades.index(old_grade)
                self.students[name].grades[index] = new_grade
                print(f"Grade updated from {old_grade} to {new_grade} for student {name}.")
            else:
                print("Old grade not found.")
        else:
            print("Student does not exist.")

    def delete_student(self, name):
        if name in self.students:
            del self.students[name]
            print(f"Student {name} deleted successfully.")
        else:
            print("Student does not exist.")

    def view_all_students(self):
        if not self.students:
            print("No students found.")
        else:
            for name, student in self.students.items():
                grades = student.view_grades()
                average = student.calculate_average()
                print(f"Student: {name}, Grades: {grades}, Average: {average:.2f}")

def main():
    gms = GradeManagementSystem()

    while True:
        print("\nStudent Grade Management System")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. View Student Grades")
        print("4. Update Grade")
        print("5. Delete Student")
        print("6. View All Students")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            gms.add_student(name)
        elif choice == '2':
            name = input("Enter student name: ")
            grade = float(input("Enter grade: "))
            gms.add_grade(name, grade)
        elif choice == '3':
            name = input("Enter student name: ")
            gms.view_student(name)
        elif choice == '4':
            name = input("Enter student name: ")
            old_grade = float(input("Enter old grade: "))
            new_grade = float(input("Enter new grade: "))
            gms.update_grade(name, old_grade, new_grade)
        elif choice == '5':
            name = input("Enter student name to delete: ")
            gms.delete_student(name)
        elif choice == '6':
            gms.view_all_students()
        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
