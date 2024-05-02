class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def average_salary(self):
        total_salary = sum(employee.salary for employee in self.employees)
        return total_salary / len(self.employees) if self.employees else 0


# Пример использования
department = Department("IT")

employee1 = Employee("John", 50000)
employee2 = Employee("Alice", 60000)
employee3 = Employee("Bob", 55000)

department.add_employee(employee1)
department.add_employee(employee2)
department.add_employee(employee3)

print("Средняя зарплата в отделе:", department.average_salary())
