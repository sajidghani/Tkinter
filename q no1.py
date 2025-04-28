class Student:
    def __init__(self,id,name,semester,ph_no):
        self.id = id
        self.name = name
        self.semester =semester
        self.ph_no = ph_no

    def course(self,course_name):
        self.course_name = course_name
        print(f'{self.name} belonging to this ID: {self.id} is studing in this course: {self.course_name}')

    def add_course(self,course_name):
        self.


stu1 = Student('101','Sajid','3rd','03323372553')
stu1.course('Programming')