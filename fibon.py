import threading
import time


def sleeper(n, name):
    print('Hi, {} is going to sleep for {} sec'.format(name, n))
    time.sleep(n)
    print('{} has woken up ..'.format(name))


# t = threading.Thread(target=sleeper, name='thread_1', args=(5, 'thread_1'))
#
# t.start()
thread_list = []

start = time.time()
for i in range(5):
    t = threading.Thread(target=sleeper, name='thread_{}'.format(i), args=(5, 'thread_{}'.format(i)))
    t.start()
    thread_list.append(t)
    print('{} has started'.format(t.name))

for t in thread_list:
    t.join()

end = time.time()

print("time taken is : {}".format(end - start))
print('all the threads have completed')
