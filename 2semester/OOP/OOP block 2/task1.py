class Student:
    def __init__(self, name, id=None):
        self.name = name
        self.id = hash(name) if id == None else id
        self.finished_courses = []

    def enrol(self, course):
        course.add_student(self)

    def remove_course(self, course):
        course.remove_student(self)

    def print_finished_courses(self):
        print(self.finished_courses)

    def __repr__(self):
        return "Student('{}:{}')".format(self.name, self.id)


class Course:
    def __init__(self, name, instructor, max_students):
        self.name = name
        self.instructor = instructor
        self.max_students = max_students
        self.students = []

    def add_student(self, *students):
        if len(self.students) < self.max_students:
            for student in students:
                if student not in self.students:
                    self.students.append(student)

    def remove_student(self, *students):
        # При удалении, считается, что студент окончил курс
        for student in students:
            if student in self.students:
                student.finished_courses.append(self)
                self.students.remove(student)

    def print_students(self):
        print(self.students)

    def __repr__(self):
        return "Course ('{}', '{}', {})".format(self.name, self.instructor, self.max_students)


science = Course('Science', 'Mary', 2)
alex = Student('Alex')
test = Student('Test', 1)
science.add_student(alex)
science.print_students()
test.enrol(science)
science.print_students()
test.print_finished_courses()
science.remove_student(test)
test.print_finished_courses()
