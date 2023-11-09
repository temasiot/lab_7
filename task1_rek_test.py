from unittest import TestCase, main
from task1_rek import sum_za_cruterijamu


class Test(TestCase):
    def test_func(self):
        a = [[22, -9, -34, -13, 10, 49], [46, -25, 8, -5, -38, -36], [15, 7, 50, -12, -39, 32], [-32, -7, 10, -9, -38, 33], [27, 24, 33, 13, 22, 0], [47, 5, 3, 25, 17, 49], [-13, 31, 42, 4, 45, 0]]
        b = ([[0, 0, 0, 0, 10, 0], [0, 0, 0, 0, 0, 0], [15, 0, 50, 0, 0, 0], [0, 0, 10, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 5, 0, 25, 0, 0], [0, 0, 0, 0, 45, 0]], 199, 35)
        self.assertEqual(sum_za_cruterijamu(a, 7, 6, 0, 0, 0, 0), b)


if __name__ == "__main__":
    main()
