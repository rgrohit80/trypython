import threading

x = 0

def thread_task():
    global x
    for i in range(100000):
        # lock.acquire()
        x += 1
        # lock.release()


def main_task():
    global x
    x = 0
    # lock = threading.Lock()
    t1 = threading.Thread(target=thread_task)
    t2 = threading.Thread(target=thread_task)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    for i in range(10):
        main_task()
        print('for the iteration {}, the value of x is: {}'.format(i, x))

# import threading
# import os
#
#
# def task1():
#     print('task1 is assigned to {}'.format(threading.current_thread().name))
#     print('ID of the process running tassk1 is {}'.format(os.getpid()))
#
#
# def task2():
#     print('task2 is assigned to {}'.format(threading.current_thread().name))
#     print('ID of the process running task2 is {}'.format(os.getpid()))
#
#
# if __name__ == '__main__':
#     print('The main thread is {}'.format(threading.main_thread().name))
#     print('ID of the process running the main thread is {}'.format(os.getpid()))
#     t1 = threading.Thread(target=task1, name='t1')
#     t2 = threading.Thread(target=task2, name='t2')
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()

# import time
# import threading
#
#
# def fun1(count):
#     for i in range(count):
#         print('fun1 sleep for 2 sec')
#         time.sleep(2)
#         print('fun_1 is awake')
#
#
# def fun2(count):
#     for i in range(count):
#         print('fun2 sleep for 1 sec')
#         time.sleep(2)
#         print('fun2 is awake now')
#
#
# if __name__ == '__main__':
#     thread1 = threading.Thread(target=fun1, args=(3,))
#     thread2 = threading.Thread(target=fun2, args=(5,))
#     thread1.start()
#     thread2.start()
#     thread1.join()
#     thread2.join()
#     print('Done...!!')
