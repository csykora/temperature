import unittest
import sys
sys.path.append("../")
from temperature_convert.temperature_convert import convert_temp_units

class TemperatureConvertTestCase(unittest.TestCase):
    """Tests for `temperature_convert.py`."""

    resultf212 = { 'Fahrenheit': 212, 'Kelvin': 373.15000000000003, 'Rankine': 671.6700000000001, 'Celsius': 100}
    def test_convert_temp_units_fahrenheit212(self):
        """Test for convert_temp_units for Fahrenheit 212 returns correct results?"""
        self.assertDictEqual(convert_temp_units(212, "Fahrenheit", False), self.resultf212)

    resultf32 = { 'Fahrenheit': 32, 'Kelvin': 273.15, 'Rankine': 491.67, 'Celsius': 0}
    def test_convert_temp_units_fahrenheit32(self):
        """Test for convert_temp_units for Fahrenheit 32 returns correct results?"""
        self.assertDictEqual(convert_temp_units(32, "Fahrenheit", False), self.resultf32)

    resultk373 = { 'Fahrenheit': 211.99999999999994, 'Kelvin': 373.15, 'Rankine': 671.67, 'Celsius': 99.99999999999997}
    def test_convert_temp_units_kelvin372(self):
        """Test for convert_temp_units for Kelvin 373 returns correct results?"""
        self.assertDictEqual(convert_temp_units(373.15, "Kelvin", False), self.resultk373)

if __name__ == '__main__':
    unittest.main()
