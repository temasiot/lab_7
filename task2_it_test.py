from unittest import TestCase, main
from task2_it import min_in_glow


class Test(TestCase):
    def test_func(self):
        a = [[82, 57, 29, 74, 21, 43, 55, 69, 9, 3], [86, 25, 45, 2, 63, 3, 11, 75, 32, 8], [19, 76, 28, 62, 85, 73, 98, 22, 14, 6], [34, 83, 51, 5, 12, 43, 26, 70, 4, 92], [40, 16, 4, 85, 91, 42, 15, 39, 1, 11], [2, 36, 29, 32, 70, 83, 46, 6, 50, 46], [6, 13, 25, 8, 90, 74, 32, 8, 78, 61], [41, 71, 24, 71, 83, 44, 23, 87, 41, 33], [27, 74, 84, 95, 28, 66, 8, 41, 88, 58], [35, 63, 80, 86, 74, 35, 69, 74, 66, 51]]
        self.assertEqual(min_in_glow(a, 10, 101), 5)


if __name__ == "__main__":
    main()
