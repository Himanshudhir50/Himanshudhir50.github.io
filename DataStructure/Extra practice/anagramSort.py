import time


def anagramSort(s1, s2):
    start = time.time()
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()
    pos = 0
    match = True

    if len(s1) == len(s2):
        while pos < len(s1) and match:
            if alist1[pos] == alist2[pos]:
                pos = pos + 1

            else:
                match = False
    else:
        match = False

    end = time.time()
    return match, end - start


if __name__ == '__main__':
    print(anagramSort('abcd', 'dcba'))
