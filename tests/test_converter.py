import unittest
from tests.java.java_server import JavaServer

from py4j.java_gateway import JavaGateway

from patternconverter import PatternConverter


class ConverterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.java_gateway = JavaServer()
        cls.java_gateway.run_server()

    @classmethod
    def tearDownClass(cls):
        cls.java_gateway.shutdown_server()

    def setUp(self):
        self.gateway = JavaGateway()

    def test_year_month_day_format_conversion_to_java(self):
        date = "2018-11-07"

        python_format = "%Y-%M-%d"
        c = PatternConverter()
        converted_format = c.convert_to_iso_8601(pattern=python_format)

        dt_formatter = self.gateway.jvm.java.time.format.DateTimeFormatter
        formatter = dt_formatter.ofPattern(converted_format)

        self.assertEqual(date.format(formatter), date)

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
