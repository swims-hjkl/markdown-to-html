import unittest

from main import extract_title


class TestExtractTitle(unittest.TestCase):

    def test_one_title(self):
        expected = "This is a title"
        actual = extract_title("## This is not a title.\n# This is a title")
        self.assertEqual(expected, actual)
