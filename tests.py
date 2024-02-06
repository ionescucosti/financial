import unittest

from database import get_instrument_modifier, instrument_modifiers, update_instrument_modifiers
from main import process_input_file
from calculation import calculate_statistics


class Tests(unittest.TestCase):
    sample_data = '''
    INSTRUMENT1,01-Jan-1996,2.4655
    INSTRUMENT1,02-Jan-1996,2.4685
    INSTRUMENT1,03-Jan-1996,2.473
    INSTRUMENT2,27-Mar-2000,9.633853443
    INSTRUMENT2,28-Mar-2000,9.627869119
    INSTRUMENT3,04-Mar-2005,104.6469
    INSTRUMENT3,19-Feb-2014,102.27
    INSTRUMENT4,17-Feb-2014,109.9
    INSTRUMENT4,18-Feb-2014,102.34
    INSTRUMENT4,19-Feb-2014,102.27
    INSTRUMENT5,02-Sep-1996,2.7415
    INSTRUMENT5,03-Sep-1996,2.7495
    '''

    expected_result = {
        "INSTRUMENT1": 2.469,
        "INSTRUMENT3": 206.9169,
        "INSTRUMENT4": 314.51,
        "INSTRUMENT5": 5.491
    }

    wrong_result = {
        "INSTRUMENT1": 314.51 ,
        "INSTRUMENT3": 206.9169,
        "INSTRUMENT4": 2.469,
        "INSTRUMENT5": 5.491
    }

    def test_process_input_file(self):
        actual_result = process_input_file('dummy_path.txt')
        self.assertEqual(self.expected_result, actual_result)

    def test_process_input_file_wrong_data(self):
        actual_result = process_input_file('dummy_path_wrong.txt')
        self.assertNotEqual(self.expected_result, actual_result)

    def test_calculate_statistics(self):
        actual_result = calculate_statistics(self.sample_data)
        self.assertEqual(self.expected_result, actual_result)

    def test_calculate_statistics_invalid_data(self):
        actual_result = calculate_statistics(self.sample_data)
        self.assertNotEqual(self.wrong_result, actual_result)


if __name__ == '__main__':
    unittest.main()
