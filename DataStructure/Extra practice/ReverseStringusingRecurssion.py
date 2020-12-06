def reverse(string):
    if len(string) == 0:
        h = print("you have empty String")
        return h

    else:
        temp  = string[0]
        reverse(string[1:])
        print(temp, end='')

if __name__ == '__main__':
    string = ""
    reverse(string)
