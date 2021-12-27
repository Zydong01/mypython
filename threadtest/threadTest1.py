
import threading
import time

def fun1(f1Num):
    for i in range(5):
        print("fun1:"+f1Num)
        time.sleep(2)

def fun2(f2Num):
    for i in range(5):
        print("fun2:"+f2Num)
        time.sleep(2)

def main():
    arg1 = "11111"
    arg2 = "22222"
    t_fun1 = threading.Thread(target=fun1, name="函数一", args=(arg1,))
    t_fun2 = threading.Thread(target=fun2, name="函数二", args=(arg2,))
    t_fun1.start()
    t_fun2.start()
    t_fun1.join()
    t_fun2.join()

main()