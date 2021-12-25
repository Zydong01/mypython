


class Pycharm:
    def excute(self):
        print("使用pycharm执行")

class Eclipse:
    def excute(self):
        print("使用eclipse执行")


class Laptop:

    def run(self, ide):
        ide.excute()


lap1 = Laptop()

ide = Eclipse()

lap1.run(ide)