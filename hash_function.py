def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])

    return sum % tablesize


if __name__ == '__main__':
    hash("Himanshu", 11)
