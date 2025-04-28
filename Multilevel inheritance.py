class GrandParent:
    def __init__(self):
        self.grand_parent_name = 'Akbar'

class Parent(GrandParent):
    def __init__(self):
        super().__init__() #invoking the constructor of the grandparent class by super method
        self.parent_name = 'Balach'

class Child(Parent):
    def __init__(self):
        super().__init__() #invoking the constructor of the parent class by super method
        self.child_name = 'Hammal'
    def show_family(self):
     print(f'Grandparent: {self.grand_parent_name}, Parent: {self.parent_name}, Child: {self.child_name}')


child = Child()
child.show_family()
parent = Parent()
