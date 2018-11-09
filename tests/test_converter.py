import unittest
from tests.java.java_server import JavaServer

from py4j.java_gateway import JavaGateway

from patternconverter import PatternConverter


class ConverterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.java_gateway_server = JavaServer()
        cls.java_gateway_server.run_server()

    @classmethod
    def tearDownClass(cls):
        cls.java_gateway_server.shutdown_server()

    def setUp(self):
        self.gateway = JavaGateway()
        self.app = self.gateway.entry_point

    def test_year_month_day_format_conversion_to_java(self):
        date = "2018-11-07"

        python_format = "%Y-%m-%d"
        c = PatternConverter()
        converted_format = c.convert_to_iso_8601(pattern=python_format)

        java_date = self.app.formatDate(date, converted_format)
        self.assertEqual(java_date, date)

    def test_python_to_iso_8601(self):
        python_format = '%Y%m%d'
        c = PatternConverter()
        converted_format = c.convert_to_iso_8601(pattern=python_format)
        expected_format = 'yyyyMMdd'
        self.assertEqual(expected_format, converted_format)

    def test_python_to_extended_iso_8601(self):
        python_format = '%Y-%m-%d'
        c = PatternConverter()
        converted_format = c.convert_to_iso_8601(pattern=python_format)
        expected_format = 'yyyy-MM-dd'
        self.assertEqual(expected_format, converted_format)
