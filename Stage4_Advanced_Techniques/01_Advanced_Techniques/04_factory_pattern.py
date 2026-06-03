# 工厂模式
class Person:
    pass

class Worker(Person):
    pass

class Teacher(Person):
    pass

class Student(Person):
    pass

class PersonFactory:
    def get_person(self, p_type):
        if p_type == "worker":
            return Worker()
        elif p_type == "teacher":
            return Teacher()
        elif p_type == "student":
            return Student()

pf = PersonFactory()
worker = pf.get_person("worker")
teacher = pf.get_person("teacher")
student = pf.get_person("student")