import unittest
import square


class TestSquare(unittest.TestCase):

    def test_area_0(self):
        self.assertEqual(square.area(0), 0)

    def test_area_1(self):
        self.assertEqual(square.area(1), 1)

    def test_area_2(self):
        self.assertEqual(square.area(2), 4)

    def test_area_5(self):
        self.assertEqual(square.area(5), 25)

    def test_area_10(self):
        self.assertEqual(square.area(10), 100)

    def test_perimeter_0(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_perimeter_1(self):
        self.assertEqual(square.perimeter(1), 4)

    def test_perimeter_2(self):
        self.assertEqual(square.perimeter(2), 8)

    def test_perimeter_5(self):
        self.assertEqual(square.perimeter(5), 20)

    def test_perimeter_10(self):
        self.assertEqual(square.perimeter(10), 40)


if __name__ == '__main__':
    unittest.main()