import unittest

from shows import available_shows

class TestAvailableShowsMethods(unittest.TestCase):

    def test_get_all_episodes(self):
        expected = {'show': 'Mr.Robot', 'season': 1, 'episode': 1}
        actual = None
        self.assertEqual(expected, actual)

    def test_get_all_seasons(self):
        expected = ['1', '2', '3']
        actual = None
        self.assertEqual(expected, actual)

    def test_get_all_shows(self):
        expected = []
        actual = None
        self.assertEqual(expected, actual)
    def test_show_available(self):
        expected = True
        actual = None
        self.assertEqual(expected,actual)
    def test_
