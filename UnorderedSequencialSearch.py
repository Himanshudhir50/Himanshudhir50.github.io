def unorderedsequencialsearch(alist, item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True

        else:
            pos = pos + 1

    return found

if __name__ == '__main__':
    Testlist = [3,4,5,5,6,7,8,8,423]
    print(sequencialsearch(Testlist, 55))
