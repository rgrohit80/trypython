import time

startT = time.time()


def myGen(n):
    for i in range(n):
        yield i


def myIter(n):
    for i in range(n):
        pass


def main():
    n = 100000
    startT = time.time()
    myIter(n)
    print('myIter took ', time.time() - startT)

    startT = time.time()
    myGen(n)
    print('myGen(n) took ', time.time() - startT)

main()
