class Persona:
    def __init__(self,id,name):
        self.name=name
        self.id=id
    def v(self):
        print("\nID:",self.id,"Имя:",self.name)
class Group():
    def __init__(self,group="ИВТ-21-1Б"):
        self.group=group
    def gr(self):
        print("Группа:",str(self.group))
class Student(Persona):
    def __init__(self, id, name):
        super().__init__(id,name)
        self.group=Group()
    def vst(self):
        print("Студент")
class Professor(Persona):
    def __init__(self, id, name):
        super().__init__(id,name)
    def vpr(self):
        print("Профессор")
student=Student(12,"Станислав")
professor=Professor(13,"Дмитрий")
student.v()
student.vst()
student.group.gr()
professor.v()
professor.vpr()





