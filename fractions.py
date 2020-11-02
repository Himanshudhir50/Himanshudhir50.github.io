def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn

    return n


class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def get_numerator(self):
        return self.num

    def get_denominator(self):
        return self.num

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + otherfraction.num * self.den
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // newden)

    def __mul__(self, otherfraction):
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den

        return Fraction(newnum, newden)

    def __sub__(self, otherfraction):
        newnum = self.num * otherfraction.den - otherfraction.num * self.den
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // newden)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num

        return firstnum == secondnum


if __name__ == '__main__':
    Fraction(1, 2)

    x = Fraction(1, 2)
    y = Fraction(3, 4)

    print(x + y)
    print(x == y)
    print(x - y)
    print(x * y)
