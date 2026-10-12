# Week 2 | Class 02: Classes, objects, constructors and inheritance

class Student:
    school = "NAVTTC AI Course"  # class variable

    def __init__(self, name, marks):
        self.name = name          # instance variable
        self.marks = marks

    def result(self):
        return "Pass" if self.marks >= 50 else "Needs practice"

    def __str__(self):
        return f"{self.name}: {self.marks} ({self.result()})"

class DataScienceStudent(Student):
    def __init__(self, name, marks, specialty):
        super().__init__(name, marks)
        self.specialty = specialty

    def result(self):
        base_result = super().result()
        return f"{base_result}; specialty: {self.specialty}"

student1 = Student("Ali", 74)
student2 = DataScienceStudent("Sara", 91, "NLP")

print(student1)
print(student2)
print("School:", Student.school)

# Composition: a course owns a list of students
class Course:
    def __init__(self, title):
        self.title = title
        self.students = []

    def enroll(self, student):
        self.students.append(student)

    def show_students(self):
        for student in self.students:
            print(student.name, "-", student.marks)

course = Course("Machine Learning")
course.enroll(student1)
course.enroll(student2)
print("\nEnrolled students:")
course.show_students()
