class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.lap = self.Computer()
    class Computer:
        def __init__(self):
            self.type = 'hp'
            self.ram = 8


s1 = Student("zhao", 22)
s2 = Student("xue", 23)
print(s1.name, s1.age, s2.name, s2.age)
print(id(s1), id(s2))

lap1 = s1.lap
lap2 = s2.lap
print(id(lap1), id(lap2))
print(lap1.ram,lap2.ram)

lap5 = s1.Computer
print(lap5)

lap3 = Student.Computer()
lap4 = Student.Computer()
print(id(lap3), id(lap4))
