class Student:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def info(self):
        print(self.num1,self.num2)

    def __add__(self, other):
        self.num1 = self.num1+other.num1
        self.num2 = self.num2+other.num2
        return self
    #
    # def __gt__(self, other):
    #     if self.num1 > other.num1 and self.num2 > other.num2:
    #         return True
    #     else:
    #         return False

s1 = Student(54,65)
s2 = Student(34,45)

if s1 > s2:
    print("s1 win")
else:
    print("s2 win")

