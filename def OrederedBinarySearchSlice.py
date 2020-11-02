def OrederedBinarySearchSlice(alist, item):
    if len(alist) == 0:

        return False

    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return OrederedBinarySearch(alist[:midpoint], item)

            else:
                return OrederedBinarySearch(alist[midpoint + 1:], item)


if __name__ == '__main__':
    alist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    Funlist = []
    print(OrederedBinarySearch(alist, 10))
    print(OrederedBinarySearch(Funlist, 9))
    print(OrederedBinarySearch(alist, 9))
