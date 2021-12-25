
class A:
    def __init__(self):
        print("A - init")

    def feature1(self):
        print("A - feature1")

class B:
    def __init__(self):
        print("B - init")
    def feature2(self):
        print("B - feature2")

class C(B,A):
    def __init__(self):
        super().__init__()
        print("C - init")

    def feature3(self):
        print("C - feature2")

c1 = C()
