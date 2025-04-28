class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)  # Initialize Person
        self.emp_id = emp_id

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)  # Initialize Person
        self.student_id = student_id

class WorkingStudent(Employee, Student):
    def __init__(self, name, emp_id, student_id):
        # Call both Employee and Student initializers
        Employee.__init__(self, name, emp_id)
        Student.__init__(self, name, student_id)

    def show_detail(self):
        return f'Name: {self.name}, Employee ID: {self.emp_id}, Student ID: {self.student_id}'

# Test the classes
student = Student('Zaheer', 102)
employee = Employee('Sameer', 109)
print(student.name, ':', student.student_id)  # Output: Zaheer : 102
print(employee.name, ':', employee.emp_id)   # Output: Sameer : 109

