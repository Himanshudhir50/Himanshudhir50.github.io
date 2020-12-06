from pythonds.basic import Stack


def DivideBy2(DecNumber, base):
    digits = "0123456789ABCDEF"
    s = Stack()

    while DecNumber > 0:
        rem = DecNumber % base
        s.push(rem)
        DecNumber = DecNumber // base

    binString = ''
    while not s.isEmpty():
        binString = binString + digits[s.pop()]

    return binString


if __name__ == '__main__':
    print(DivideBy2(26,26))
