import unittest
import os

from patternconverter import PatternConverter


class ConverterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def test_python_to_iso_8601(self):
        python_format = '%Y%M%d'
        c = PatternConverter()
        converted_format = c.convert_to_iso_8601(pattern=python_format)
        expected_format = 'yyyymmdd'
        self.assertEqual(converted_format, expected_format)

    def test_python_to_extended_iso_8601(self):
        python_format = '%Y-%M-%d'
        c = PatternConverter()
        converted_format = c.convert_to_iso_8601(pattern=python_format)
        expected_format = 'yyyy-mm-dd'
        self.assertEqual(converted_format, expected_format)
