""""
    unit test class for Fraction class
"""

import unittest

from fractions import Fraction


class TestFraction(unittest.TestCase):
    """
       First we setup our test
       """

    def setUp(self):
        self.f1 = Fraction(3, 4)
        self.f2 = Fraction(-1, 4)
        self.f3 = Fraction(-5, -4)
        self.f4 = Fraction(9, -4)
        self.f5 = Fraction(-3, 4)

    def tearDown(self):

        """
        Teardown will cleanup everything after each test
        """
        pass

    def test_init(self):
        """
          Test for the __init__ method
        """
        fail = False

        try:
            f = Fraction(1, 0)
        except ValueError:
            fail = True

        self.assertTrue(fail)
        self.assertTrue(self.f5.num == -3)
        self.assertTrue(self.f5.den == 4)

    def test_init_type(self):
        fail = False

        try:
            f = Fraction(1.0, 3)
        except TypeError:
            fail = True

        self.assertTrue(fail)

    def test_add(self):
        self.assertEqual(self.f1 + self.f2, Fraction(2, 4))
        self.assertEqual(self.f2 + self.f3, Fraction(4, 4))
        self.assertEqual(self.f3 + self.f5, Fraction(2, 4))
        self.assertEqual(self.f4 + self.f2, Fraction(-8, 4))

    def test_eq(self):
        self.assertNotEqual(self.f1, self.f2)
        self.assertEqual(self.f2, self.f3)
        self.assertEqual(self.f2, self.f5)
        self.assertEqual(Fraction(-1, 2), Fraction(1, -2))
        self.assertEqual(Fraction(-1, -2), Fraction(1, 2))

    def test_mul(self):
        self.assertEqual(self.f1 * self.f2, Fraction(1, 8))
        self.assertEqual(self.f3 * self.f4, Fraction(-1, 20))

    if __name__ == "__main__":
        unittest.main()
