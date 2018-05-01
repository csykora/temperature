import unittest
import sys
sys.path.append("../")
from temperature_convert.temperature_convert import valid_student_response

class TemperatureConvertTestCase(unittest.TestCase):
    """Tests for `temperature_convert.py`."""

    def test_valid_student_response_is_number(self):
        """Test for valid_student_response is number?"""
        self.assertTrue(valid_student_response(100.0, False))

    def test_valid_student_response_fails_when_not_number(self):
        """Test for valid_student_response is not number?"""
        self.assertRaises(SystemExit, valid_student_response, "Invalid", False)

if __name__ == '__main__':
    unittest.main()
