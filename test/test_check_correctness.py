import unittest
import sys
sys.path.append("../")
from temperature_convert.temperature_convert import check_correctness
from temperature_convert.temperature_convert import convert_temp_units

class TemperatureConvertTestCase(unittest.TestCase):
    """Tests for `temperature_convert.py`."""

    def test_check_correctness_is_correct_when_equal(self):
        """Test for check_correctness is correct when equals?"""
        # create conversion for f212
        temps = convert_temp_units(212, "Fahrenheit", False)
        self.assertEquals( check_correctness('Celsius', 100.0, temps, False) , "correct")

    def test_check_correctness_is_incorrect_when_not_equal(self):
        """Test for check_correctness is incorrect when not equals?"""
        # create conversion for f212
        temps = convert_temp_units(212, "Fahrenheit", False)
        self.assertRaises( SystemExit, check_correctness, 'Celsius', 0.0, temps, False)

if __name__ == '__main__':
    unittest.main()
