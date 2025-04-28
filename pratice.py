import csv


class Employee:
    def __init__(self, name, age, department):
        self.name = name
        self.age = int(age)  # Convert age to an integer
        self.department = department

    def __str__(self):
        return f"Employee Name: {self.name}, Age: {self.age}, Department: {self.department}"

    @classmethod
    def from_csv(cls, csv_file):
        # List to store the created instances
        employees = []

        # Open the CSV file
        with open(csv_file, mode='r') as file:
            # Create a CSV reader object
            csv_reader = csv.DictReader(file)

            # Read each row from the CSV file
            for row in csv_reader:
                # For each row, create an Employee instance and append it to the list
                employee = cls(row['Name'], row['Age'], row['Department'])
                employees.append(employee)

        return employees


# Using the class method to create instances from a CSV file
employees = Employee.from_csv('employees.csv')

# Printing the created instances
for employee in employees:
    print(employee)
