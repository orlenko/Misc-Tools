import unittest

from .. import dummy_util


class MyTestCase(unittest.TestCase):
    def test_some_dummy_calculation(self):
        calculated = dummy_util.some_dummy_calculation()
        self.assertEqual(calculated, 42)


if __name__ == '__main__':
    unittest.main()
