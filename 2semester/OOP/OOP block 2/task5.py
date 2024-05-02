class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"


class Employee:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary

    def display_employee(self):
        return f"Employee ID: {self.emp_id}, Salary: {self.salary}"


class Student:
    def __init__(self, student_id, grade):
        self.student_id = student_id
        self.grade = grade

    def display_student(self):
        return f"Student ID: {self.student_id}, Grade: {self.grade}"


class PersonInfo(Person, Employee, Student):
    def __init__(self, name, age, emp_id, salary, student_id, grade):
        Person.__init__(self, name, age)
        Employee.__init__(self, emp_id, salary)
        Student.__init__(self, student_id, grade)

    def display_info(self):
        return f"{Person.display_info(self)}, {Employee.display_employee(self)}, {Student.display_student(self)}"


# Пример использования
person_info = PersonInfo("John", 30, "E123", 50000, "S456", "A")
print(person_info.display_info())
