class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age   # Encapsulation

    def get_info(self):
        return "Name: " + self.name + ", Age: " + str(self._age)


class Student(Person):   # Inheritance
    def __init__(self, name, age, grade):
        Person.__init__(self, name, age)
        self.grade = grade

    # polymorphism
    def get_info(self):
        return "Student: " + self.name + ", Age: " + str(self._age) + ", Grade: " + str(self.grade)



name_p = input("Enter person name: ")
age_p = int(input("Enter person age: "))

p = Person(name_p, age_p)

name_s = input("Enter student name: ")
age_s = int(input("Enter student age: "))
grade_s = int(input("Enter student grade: "))

s = Student(name_s, age_s, grade_s)


print(p.get_info())
print(s.get_info())