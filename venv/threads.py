import threading
import time


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        # Get lock to synchronize threads
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        # Free lock to release next thread
        threadLock.release()


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for t in threads:
    t.join()
print("Exiting Main Thread")


--------------------------------

import threading
import time


class myThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):

        threadLock.acquire()
        print("Starting  {}".format(self.name))
        print_name(self.name, self.delay)
        print("Existing {}".format(self.name))
        threadLock.release()


def print_name(name, delay):
    time.sleep(delay)
    print("%s: %s" % (name, time.ctime(time.time())))


threadLock = threading.Lock()

threads = []

thread1 = myThread('thread_1', 10)
thread2 = myThread('thread_2', 5)

threads.append(thread1)
threads.append(thread2)

for t in threads:
    t.start()

for t in threads:
    t.join()
print("Exiting Main Thread")

