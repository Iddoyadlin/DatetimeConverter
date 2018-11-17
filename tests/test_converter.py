import unittest
from py4j.java_gateway import JavaGateway

from tests.java.java_server import JavaServer
from py2jdatetime2.patternconverter import PatternConverter


class ConverterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Run the java gateway server to allow testing java generated patterns
        cls.java_gateway_server = JavaServer()
        cls.java_gateway_server.run_server()

    @classmethod
    def tearDownClass(cls):
        cls.java_gateway_server.shutdown_server()

    def setUp(self):
        # Create a connection to the java geateway to get access to the jvm
        self.gateway = JavaGateway()
        # Save a ref to the java gateway server class to access the functions we defined in it for tests
        self.app = self.gateway.entry_point

    def test_valid_pattern_year_month_day_with_delimiter_conversion_python_to_iso_8601(self):
        date = "2018-11-07"

        python_pattern = "%Y-%m-%d"
        c = PatternConverter()
        converted_pattern = c.convert_to_iso_8601(pattern=python_pattern)

        iso_date = self.app.formatDate(date, converted_pattern)
        self.assertEqual(iso_date, date)

    def test_valid_pattern_year_month_day_conversion_python_to_iso_8601(self):
        python_pattern = '%Y%m%d'
        c = PatternConverter()
        converted_pattern = c.convert_to_iso_8601(pattern=python_pattern)
        expected_format = 'yyyyMMdd'
        self.assertEqual(expected_format, converted_pattern)
