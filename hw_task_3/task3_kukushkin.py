#task 1
# 1.	Создайте класс  прямоугольника. Класс принимает два параметра, ширина и высота прямоугольника.
# Создайте два метода:
# -	метод возвращающий площадь прямоугольника
# -	метод возвращающий периметр прямоугольника

class Rectangle:
    def __init__(self, side):
        self.side =side

    def count_area(self):
        print(self.side**2)
    def count_perimeter(self):
        print(self.side * 4)


ca = Rectangle(2)
#ca.count_area()
#ca.count_perimeter()

# task 2

class Teacher:
    def __init__(self):
        self.students_number = 0

    def teach(self, material_name, *students):
        for student in students:
            student.take(material_name)
            self.students_number + 1
class Student:
    def __init__(self):
        self.knowledge = []
    def take(self, material_name):
        self.knowledge.append(material_name)

class StudyMaterials:
    def __init__(self, *material_name):
        self.materials = list(material_name)


teacher = Teacher()
student1 = Student()
student2 = Student()
student3 = Student()
student4 = Student()
obj = StudyMaterials('Python','Version Control Systems', 'Relational Databases', 'NoSQL databases', 'Message Brokers')


teacher.teach('Python', student1, student2)
teacher.teach('Version Control Systems', student3, student4)
teacher.teach('NoSQL databases', student2, student3, student4)
teacher.teach('Relational Databases', student1, student2, student3, student4)
teacher.teach('Message Brokers', student1)
print(student1.knowledge)
print(student4.knowledge)

#task 3

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender



class Teacher (Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.students_number = 0

    def teach(self, material_name, *students):
        for student in students:
            student.take(material_name)
            self.students_number + 1


class Student (Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.knowledge = []
    def take(self, material_name):
        self.knowledge.append(material_name)
    def __len__(self):
        return len(self.knowledge)
    def forget(self):
        import random
        if self.knowledge:
            forgotten_index = random.randint(0, len(self.knowledge) - 1)
            forgotten_knowledge = self.knowledge.pop(forgotten_index)
            print(f"Я забыл {forgotten_knowledge}")
        else:
            print("Я ничего и не знал")


class StudyMaterials:
    def __init__(self, *materials):
        self.materials = list(materials)

    def __len__(self):
        return len(self.materials)


teacher = Teacher('Иван', 45, 'М')
student1 = Student('Петр', 20, 'М')
student2 = Student('Мария', 19, 'Ж')
student3 = Student('Захар', 18, 'М')
student4 = Student('Анна', 21, 'Ж')
obj = StudyMaterials('Python','Version Control Systems', 'Relational Databases', 'NoSQL databases', 'Message Brokers')


teacher.teach('Python', student1, student2)
teacher.teach('Version Control Systems', student3, student4)
teacher.teach('NoSQL databases', student2, student3, student4)
teacher.teach('Relational Databases', student1, student2, student3, student4)
teacher.teach('Message Brokers', student1)



print(student1.knowledge)
print(student4.knowledge)
print(len(obj))
print(len(student1))

student1.forget()
student1.forget()
student1.forget()
student1.forget()
print(student1.knowledge)