from unittest import TestCase, main
from task3_rek import decide


class Test(TestCase):
    def test_func(self):
        r = []
        a = [[1, 1, 2, 1, 3], [1, 1, 3, 1, -1], [2, 3, 4, 5, 6], [1, 1, 5, 1, 3], [1, 1, 6, 1, 3]]
        decide(a, 5, r, 0, 0, [])
        self.assertEqual(r, [2])


if __name__ == "__main__":
    main()
