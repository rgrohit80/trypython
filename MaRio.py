import time

startT = time.time()


def myGen(n):
    for i in range(n):
        yield i


def myIter(n):
    for i in range(n):
        pass


def main():
    n = 100000000
    startT = time.time()
    myIter(n)
    print('myIter took {} sec'.format(time.time() - startT))
    startT = time.time()
    myGen(n)
    print('myGen took {} sec'.format(time.time() - startT))


if __name__ == '__main__':
    main()
