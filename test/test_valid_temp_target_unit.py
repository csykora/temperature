import unittest
import sys
sys.path.append("../")
from temperature_convert.temperature_convert import valid_temp_target_unit

class TemperatureConvertTestCase(unittest.TestCase):
    """Tests for `temperature_convert.py`."""

    def test_valid_temp_target_unit_is_valid_unit(self):
        """Test for valid_temp_target_unit is valid unit?"""
        self.assertTrue(valid_temp_target_unit("Fahrenheit", False))
        self.assertTrue(valid_temp_target_unit("Celsius", False))
        self.assertTrue(valid_temp_target_unit("Kelvin", False))
        self.assertTrue(valid_temp_target_unit("Rankine", False))

    def test_valid_temp_target_unit_fails_when_invalid(self):
        """Test for valid_temp_target_unit is invalid?"""
        self.assertRaises(SystemExit, valid_temp_target_unit, "Invalid", False)

if __name__ == '__main__':
    unittest.main()
