import time


def concatination():
    start = time.time()
    alist = ['Himanshu','Hello']
    for i in range(10000):
        alist = alist + [i]
    end = time.time()
    return end - start, alist


def appendlist1():
    start = time.time()
    list1 = []
    for i in range(10000):
        list1.append(i)
    end = time.time()
    return end - start, list1


def comprehension1():
    start = time.time()
    list1 = [i for i in range(10000)]
    end = time.time()
    return end - start, list1


def list1():
    start = time.time()
    l = list(range(10000))
    end = time.time()
    return end - start, l


if __name__ == '__main__':
    print(concatination())
    print(appendlist1())
    print(comprehension1())
    print(list1())
