from pythonds.basic import Stack

rStack = Stack()

def toStr(n,base):
    convertString = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n % base])
        n = n // base
    String = ""
    while not rStack.isEmpty():
        String = String + str(rStack.pop())
    return String

print(toStr(1453,16))
