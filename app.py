import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext


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
            return False
        else:
            self.students[name] = Student(name)
            return True

    def add_grade(self, name, grade):
        if name in self.students:
            self.students[name].add_grade(grade)
            return True
        return False

    def view_student(self, name):
        if name in self.students:
            return self.students[name].view_grades(), self.students[name].calculate_average()
        return None, None

    def update_grade(self, name, old_grade, new_grade):
        if name in self.students:
            if old_grade in self.students[name].grades:
                index = self.students[name].grades.index(old_grade)
                self.students[name].grades[index] = new_grade
                return True
            return False
        return False

    def delete_student(self, name):
        if name in self.students:
            del self.students[name]
            return True
        return False

    def delete_grade(self, name, grade):
        if name in self.students:
            if grade in self.students[name].grades:
                self.students[name].grades.remove(grade)
                return True
            return False
        return False

    def view_all_students(self):
        return {name: (student.view_grades(), student.calculate_average()) for name, student in self.students.items()}


class StudentGradeApp:
    def __init__(self, master):
        self.master = master
        self.gms = GradeManagementSystem()
        self.master.title("Student Grade Management System")

        # Frame for adding students and grades
        self.frame = tk.Frame(master)
        self.frame.pack(pady=10)

        self.student_name_label = tk.Label(self.frame, text="Student Name:")
        self.student_name_label.grid(row=0, column=0)

        self.student_name_entry = tk.Entry(self.frame)
        self.student_name_entry.grid(row=0, column=1)

        self.add_student_button = tk.Button(self.frame, text="Add Student", command=self.add_student)
        self.add_student_button.grid(row=0, column=2)

        self.grade_label = tk.Label(self.frame, text="Grade:")
        self.grade_label.grid(row=1, column=0)

        self.grade_entry = tk.Entry(self.frame)
        self.grade_entry.grid(row=1, column=1)

        self.add_grade_button = tk.Button(self.frame, text="Add Grade", command=self.add_grade)
        self.add_grade_button.grid(row=1, column=2)

        self.view_button = tk.Button(self.frame, text="View Grades", command=self.view_student)
        self.view_button.grid(row=2, column=0, columnspan=3)

        self.update_button = tk.Button(self.frame, text="Update Grade", command=self.update_grade)
        self.update_button.grid(row=3, column=0, columnspan=3)

        self.delete_student_button = tk.Button(self.frame, text="Delete Student", command=self.delete_student)
        self.delete_student_button.grid(row=4, column=0, columnspan=3)

        self.delete_grade_button = tk.Button(self.frame, text="Delete Grade", command=self.delete_grade)
        self.delete_grade_button.grid(row=5, column=0, columnspan=3)

        self.view_all_button = tk.Button(self.frame, text="View All Students", command=self.view_all_students)
        self.view_all_button.grid(row=6, column=0, columnspan=3)

        self.result_area = scrolledtext.ScrolledText(master, width=50, height=15)
        self.result_area.pack(pady=10)

    def add_student(self):
        name = self.student_name_entry.get().strip()
        if name:
            if self.gms.add_student(name):
                messagebox.showinfo("Success", f"Student '{name}' added successfully.")
            else:
                messagebox.showwarning("Warning", f"Student '{name}' already exists.")
            self.student_name_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a student name.")

    def add_grade(self):
        name = self.student_name_entry.get().strip()
        grade_input = self.grade_entry.get().strip()
        try:
            grade = float(grade_input)
            if 0 <= grade <= 100:
                if self.gms.add_grade(name, grade):
                    messagebox.showinfo("Success", f"Grade {grade} added for student '{name}'.")
                else:
                    messagebox.showwarning("Warning", f"Student '{name}' does not exist.")
            else:
                messagebox.showwarning("Warning", "Grade must be between 0 and 100.")
        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid numeric grade.")
        self.grade_entry.delete(0, tk.END)

    def view_student(self):
        name = self.student_name_entry.get().strip()
        grades, average = self.gms.view_student(name)
        if grades is not None:
            result = f"Grades for {name}: {grades}\nAverage: {average:.2f}\n"
        else:
            result = f"Student '{name}' does not exist.\n"
        self.result_area.delete(1.0, tk.END)
        self.result_area.insert(tk.END, result)

    def update_grade(self):
        name = self.student_name_entry.get().strip()
        old_grade_input = simpledialog.askstring("Update Grade", "Enter old grade:")
        new_grade_input = simpledialog.askstring("Update Grade", "Enter new grade:")
        try:
            old_grade = float(old_grade_input)
            new_grade = float(new_grade_input)
            if self.gms.update_grade(name, old_grade, new_grade):
                messagebox.showinfo("Success", f"Grade updated from {old_grade} to {new_grade} for student '{name}'.")
            else:
                messagebox.showwarning("Warning", "Failed to update grade. Ensure the student and old grade exist.")
        except ValueError:
            messagebox.showwarning("Warning", "Please enter valid numeric grades.")

    def delete_student(self):
        name = self.student_name_entry.get().strip()
        if self.gms.delete_student(name):
            messagebox.showinfo("Success", f"Student '{name}' deleted successfully.")
        else:
            messagebox.showwarning("Warning", f"Student '{name}' does not exist.")

    def delete_grade(self):
        name = self.student_name_entry.get().strip()
        grade_input = simpledialog.askstring("Delete Grade", "Enter grade to delete:")
        try:
            grade = float(grade_input)
            if self.gms.delete_grade(name, grade):
                messagebox.showinfo("Success", f"Grade {grade} removed for student '{name}'.")
            else:
                messagebox.showwarning("Warning", "Failed to delete grade. Ensure the student and grade exist.")
        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid numeric grade.")

    def view_all_students(self):
        all_students = self.gms.view_all_students()
        result = "All Students:\n"
        if all_students:
            for name, (grades, average) in all_students.items():
                result += f"Student: {name}, Grades: {grades}, Average: {average:.2f}\n"
        else:
            result += "No students found.\n"
        self.result_area.delete(1.0, tk.END)
        self.result_area.insert(tk.END, result)


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentGradeApp(root)
    root.mainloop()
