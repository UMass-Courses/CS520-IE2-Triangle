import unittest
from isTriangle import Triangle
# import sys
# sys.path.append("..")
# from src.Triangle import Triangle

class TriangleTest(unittest.TestCase):
    def test_equilateral(self):
        actual = Triangle.classify(10, 10, 10)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    def test_isosceles(self):
        actual = Triangle.classify(10, 15, 10)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test_isosceles2(self):
        actual = Triangle.classify(15, 15, 10)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test_scalene(self):
        actual = Triangle.classify(10, 15, 12)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

    def test_negative(self):
        actual = Triangle.classify(-1, 10, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_zero(self):
        actual = Triangle.classify(0, 10, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_zero2(self):
        actual = Triangle.classify(10, 0, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_zero3(self):
        actual = Triangle.classify(10, 10, 0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_all_zero(self):
        actual = Triangle.classify(0, 0, 0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_illegal(self):
        actual = Triangle.classify(10, 10, 30)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_illegal2(self):
        actual = Triangle.classify(30, 12, 18)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_illegal3(self):
        actual = Triangle.classify(12, 18, 30)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_illegal4(self):
        actual = Triangle.classify(12, 30, 18)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_illegal_isoc(self):
        actual = Triangle.classify(15, 30, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_illegal_isoc2(self):
        actual = Triangle.classify(30, 10, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_illegal_isoc3(self):
        actual = Triangle.classify(5, 5, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_illegal_isoc4(self):
        actual = Triangle.classify(5, 10, 5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_illegal_isoc5(self):
        actual = Triangle.classify(10, 5, 5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
