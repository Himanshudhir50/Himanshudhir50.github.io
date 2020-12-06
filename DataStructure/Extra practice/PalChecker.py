from deque import Deque

"""
First we will put aString in the deque then we compare the deque 
first character and rear character until the deque get empty
"""


def palChecker(aString):
    charDeque = Deque()

    for ch in aString:
        charDeque.addRear(ch)

    StillEqual = True

    while charDeque.size() and StillEqual:
        first = charDeque.removeFront()
        last = charDeque.removeLast()

        if first != last:
            stillEqual = False

    return stillEqual


def main():
    print(palChecker("Himanshu"))
    print(palChecker("Radar"))


if __name__ == '__main__':
    main()
