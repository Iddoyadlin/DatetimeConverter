import unittest

from converter import Converter


class ConverterTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_python_to_iso_8601(self):
        python_format = '%Y%M%d'
        c = Converter()
        converted_format = c.convert_to_iso_8601(format=python_format)
        expected_format = 'yyyymmdd'
        self.assertEqual(converted_format, expected_format)
