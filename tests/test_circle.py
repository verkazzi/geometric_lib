import unittest
import circle
import math


class TestCircle(unittest.TestCase):

    def test_area_zero(self):
        self.assertEqual(circle.area(0), 0)

    def test_area_fractional(self):
        self.assertAlmostEqual(circle.area(2.5), math.pi * 2.5 ** 2)

    def test_area_large_radius(self):
        self.assertAlmostEqual(circle.area(100), math.pi * 100 ** 2)

    def test_area_small_radius(self):
        self.assertAlmostEqual(circle.area(0.01), math.pi * 0.01 ** 2)

    def test_area_doubled_radius(self):
        self.assertAlmostEqual(circle.area(4),4 * circle.area(2))

    def test_perimeter_zero(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_perimeter_fractional(self):
        self.assertAlmostEqual(circle.perimeter(2.5), 2 * math.pi * 2.5)

    def test_perimeter_large_radius(self):
        self.assertAlmostEqual(circle.perimeter(100), 2 * math.pi * 100)

    def test_perimeter_small_radius(self):
        self.assertAlmostEqual(circle.perimeter(0.01), 2 * math.pi * 0.01)

    def test_perimeter_doubled_radius(self):
        self.assertAlmostEqual(circle.perimeter(4),2 * circle.perimeter(2))


if __name__ == '__main__':
    unittest.main()