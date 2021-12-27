
import threading
import time

def fun1(f1Num):
    print("fun1:"+f1Num)

def fun2(f2Num):
    print("fun2:"+f2Num())

if __name__ == '__main__':
    t_fun1 = threading.Thread(fun1(), name="函数一", args="11111")
    t_fun2 = threading.Thread(fun2(), name="函数二", args="22222")
    t_fun1.start()
    t_fun2.start()
    t_fun1.join()
    t_fun2.join()