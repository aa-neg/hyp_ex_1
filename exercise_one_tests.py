import unittest

from exercise_one import daysBetweenDates

class unitTests(unittest.TestCase):

    def test_minimalRequirements(self):
        self.assertEqual(daysBetweenDates('02/06/1983', '22/06/1983'), 19)
        self.assertEqual(daysBetweenDates('04/07/1984', '25/12/1984'), 173)
        self.assertEqual(daysBetweenDates('03/01/1989', '03/08/1983'), 1979)

        self.assertEqual(daysBetweenDates('07/11/1972', '08/11/1972'), 0)
        self.assertEqual(daysBetweenDates('01/01/2000', '03/01/2000'), 1)


if __name__ == '__main__':

    unittest.main()