class Father:
    def __init__(self):
        self.father_name = 'Sajid'

class Mother:
    def __init__(self):
        self.mother_name = 'Sajida'

class Child(Father,Mother):
    def __init__(self):
        Father. __init__(self)
        Mother.__init__(self)
        self.child_name = 'Sadiq'
    def Family_member(self):
        print(f'Father: {self.father_name}, Mother: {self.mother_name} and Child: {self.child_name}')

child = Child()
child.Family_member()
