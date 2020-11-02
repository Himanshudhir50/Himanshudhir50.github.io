def sumOfN(n):
    thesum = 0
    for i in range(1, n + 1):
        thesum = thesum + i

    return thesum


if __name__ == '__main__':
    print(sumOfN(10))
