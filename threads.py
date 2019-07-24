import threading
import time


class myThread(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        print("Starting " + self.name)
        threadLock.acquire()
        print_time(self.name, 3)
        threadLock.release()
        print("existing " + self.name)


def print_time(name, delay):
    time.sleep(delay)
    print("%s : %s" % (name, time.ctime(time.time())))


threadLock = threading.Lock()
threads = []

thread_1 = myThread(1, "thread_1")
thread_2 = myThread(2, "thread_2")

thread_1.start()
thread_2.start()

threads.append(thread_1)
threads.append(thread_2)

for i in threads:
    i.join()
    print("existing the main thread")


