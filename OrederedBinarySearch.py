def OrederedBinarySearch(alist, item):
    if len(alist) == 0:
        print("You have Empty list")
        return False
    found = False
    first = 0
    last = len(alist) - 1

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True

        else:
            if alist[midpoint] > item:
                last = midpoint - 1

            else:
                first = midpoint + 1

    return found

if __name__ == '__main__':
    alist = [1, 2, 3, 4, 5, 6, 7]
    print(OrederedBinarySearch(alist, 5))
