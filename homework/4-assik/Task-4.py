class Employee:
    def __init__(self, salary):
        self.__salary = salary  

    def get_salary(self):
        return self.__salary

    def get_role(self):
        return "Employee"



class Manager(Employee):
    def __init__(self, salary, bonus):
        Employee.__init__(self, salary)
        self.bonus = bonus

    def get_role(self):
        return "Manager"

    def get_bonus(self):
        return self.bonus


def print_employees(arr):
    i = 0
    while i < len(arr):
        emp = arr[i]
        print(emp.get_role(), emp.get_salary())
        i = i + 1


employees = []

n = int(input("How many employees? "))

i = 0
while i < n:
    salary = int(input("Enter salary: "))
    emp = Employee(salary)
    employees.append(emp)
    i = i + 1

manager_salary = int(input("Enter manager salary: "))
manager_bonus = int(input("Enter manager bonus: "))

manager = Manager(manager_salary, manager_bonus)
employees.append(manager)

print_employees(employees)

print("Manager bonus:", manager.get_bonus())
