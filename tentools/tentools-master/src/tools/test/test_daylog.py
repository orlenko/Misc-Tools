import unittest
from datetime import datetime
from .. import daylog


class DaylogTests(unittest.TestCase):
    def test_daysum(self):
        daylog.entries.append((datetime(2002, 1, 1, 12, 23), 'Blah foo bar'))
        summary = daylog.day_summary(datetime(2002, 1, 1))
        self.assertEqual(summary, 'Day Notes for Tuesday Jan 01 2002\n\n[12:23]\tBlah foo bar')


if __name__ == '__main__':
    unittest.main()
