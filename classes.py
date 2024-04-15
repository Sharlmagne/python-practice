class Employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    def raise_salary(self, new_salary):
        self.salary = new_salary

# class Developer(Employee):
#     def __init__(self):


emp1 = Employee("Sharlmagne", "Henry", 90000)

print(emp1.firstname)
