def listsum(numlist):
    if len(numlist) == 1:
        return numlist[0]

    else:
        return numlist[0] + listsum(numlist[1:])

if __name__ == '__main__':
    print(listsum([1,2,3,4,5,6,7,8,9]))
