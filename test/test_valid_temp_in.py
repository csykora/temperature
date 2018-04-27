import unittest
import sys
sys.path.append("../")
from temperature_convert.temperature_convert import valid_temp_in

class TemperatureConvertTestCase(unittest.TestCase):
    """Tests for `temperature_convert.py`."""

    def test_valid_temp_in_requires_two_parameters(self):
        """Test for valid temp in parameters?"""
        self.assertTrue(valid_temp_in([84.2, "Fahrenheit"], False))

    def test_valid_temp_in_fails_when_not_two_parameters(self):
        """Test for in valid temp in parameters, not exactly 2 parameters?"""
        self.assertRaises(SystemExit, valid_temp_in, [84.2, "extra", "Fahrenheit"], False)
        self.assertRaises(SystemExit, valid_temp_in, [84.2], False)

    def test_valid_temp_in_first_item_is_number(self):
        """Test for first list item is number?"""
        self.assertTrue(valid_temp_in([84.2, "Fahrenheit"], False))

    def test_valid_temp_in_fails_when_first_param_is_not_number(self):
        """Test for first list item is not number?"""
        self.assertRaises(SystemExit, valid_temp_in, ["Invalid", "Fahrenheit"], False)

    def test_valid_temp_in_requires_corrent_temp_unit(self):
        """Test for valid temp in parameters?"""
        self.assertTrue(valid_temp_in([0, "Fahrenheit"], False))
        self.assertTrue(valid_temp_in([0, "Celsius"], False))
        self.assertTrue(valid_temp_in([0, "Kelvin"], False))
        self.assertTrue(valid_temp_in([0, "Rankine"], False))

    def test_valid_temp_in_fails_when_invalid_temp_unit(self):
        """Test for invalid temp unit?"""
        self.assertRaises(SystemExit, valid_temp_in, [0, "Invalid"], False)

if __name__ == '__main__':
    unittest.main()
