class Scholar:
    def __init__(self, serviceHrs):
        self.serviceHrs = serviceHrs
    def getAll(self):
        return self.serviceHrs
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    def getAll(self):
        return self.name, self.grades
class StudentLeader(Scholar, Student):
    def __init__(self, serviceHrs, name, grades, position):
        Scholar.__init__(self, serviceHrs)
        Student.__init__(self, name, grades)
        self.position = position
    def getAll(self):
        return self.position

scholarOne = StudentLeader(12, "Archie", [90, 98, 100], "Secretary")
print(Scholar.getAll(scholarOne))
print(Student.getAll(scholarOne))
print(StudentLeader.getAll(scholarOne))