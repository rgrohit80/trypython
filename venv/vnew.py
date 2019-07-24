import threading
import time


def task1(lock):
    lock.acquire()
    for i in range(5):
        time.sleep(i)
        print('TASK 1 : slept for :{} sec'.format(i))
    lock.release()
    print('task1 completed..!!')



def task2(lock):
    lock.acquire()
    for i in range(5):
        time.sleep(i)
        print('TASK 2 : slept for :{} sec'.format(i))
    lock.release()
    print('task2 completed..!!')



def main_thread():
    print('the main thread started..!!')
    lock = threading.Lock()
    t1 = threading.Thread(target=task1, args=(lock,))
    t2 = threading.Thread(target=task2, args=(lock,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

main_thread()