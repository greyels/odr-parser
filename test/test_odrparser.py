import unittest

from config import config as cfg

from src.odrparser import ODRParser


class TestODRParser(unittest.TestCase):
    def setUp(self):
        self.parser = ODRParser()

    def test_find_relevant_jds(self):
        self.parser.find_relevant_jds("static/odr.json", cfg.KEYWORD_LIST, cfg.LEVEL, cfg.NO_LANGUAGE)
        self.assertEqual(5, len(self.parser._relevant_jds))


if __name__ == '__main__':
    unittest.main()
