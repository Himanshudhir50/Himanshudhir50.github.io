"""Big of this anagram program is n^2"""
def anagram(s1, s2):
    stillok = True
    if len(s1) != len(s2):
        stillok = False

    pos1 = 0
    alist = list(s2)

    while pos1 < len(s1) and stillok:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True

            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None

        else:
            stillok = False

        pos1 = pos1 + 1

    return stillok


if __name__ == '__main__':
    print(anagram('abcd', 'dbca'))
