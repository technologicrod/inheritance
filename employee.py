class Employee():
    def __init__(self, idnumber, name, age, gender):
        self.idnumber = idnumber
        self.name = name
        self.age = age
        self.gender = gender
    def getDeets(self):
        return self.idnumber, self.name, self.age, self.gender

class FullTime(Employee):
    def __init__(self, idnumber, name, age, gender, basicpay, benefits):
        super().__init__(idnumber, name, age, gender)
        self.basicpay = basicpay
        self.benefits = benefits
    def getDeets(self):
        return self.basicpay, self.benefits
class PartTime(Employee):
    def __init__(self, idnumber, name, age, gender, hoursworked, hourlyrate):
        super().__init__(idnumber, name, age, gender)
        self.hoursworked = hoursworked
        self.hourlyrate = hourlyrate
    def getDeets(self):
        return self.hoursworked, self.hourlyrate

fulltimeOne = FullTime("01", "Daryl", 22, "Male", 30000, "SSS, Pagibig, PhilHealth")
parttimeOne = PartTime("02", "Archie", 23, "Male", 10, 200)

print(Employee.getDeets(fulltimeOne))
print(FullTime.getDeets(fulltimeOne))
print(Employee.getDeets(parttimeOne))
print(PartTime.getDeets(parttimeOne))