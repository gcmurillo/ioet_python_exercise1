import unittest
import utils
import datetime

class UtilsTests(unittest.TestCase):
    
    def test_load_data(self):
        to_compare = {
            'week': [
                ('00:01', '09:00', 25),
                ('09:01', '18:00', 15),
                ('18:01', '00:00', 20),
            ],
            'weekend': [
                ('00:01', '09:00', 30),
                ('09:01', '18:00', 20),
                ('18:01', '00:00', 25),
            ]
        }
        my_dict = {}
        utils.load_data('week', my_dict)
        utils.load_data('weekend', my_dict)
        self.assertEqual(to_compare, my_dict)

    def test_get_data_from_line(self):
        to_compare = ("ASTRID", ["MO10:00-12:00", "TH12:00-14:00"])
        data = utils.get_data_from_line("ASTRID=MO10:00-12:00,TH12:00-14:00")
        self.assertEqual(to_compare, data)

    def test_parse_time(self):
        to_compare = datetime.datetime.strptime("20:00", "%H:%M")
        data = utils.parse_time("20:00")
        self.assertEqual(to_compare, data)

    def test_is_between(self):
        initial = datetime.datetime.strptime("10:00", "%H:%M")
        final = datetime.datetime.strptime("12:00", "%H:%M")
        to_check = datetime.datetime.strptime("11:00", "%H:%M")
        self.assertEqual(True, utils.is_between(initial, final, to_check))

    def test_is_lt(self):
        initial = datetime.datetime.strptime("21:00", "%H:%M")
        final = datetime.datetime.strptime("00:00", "%H:%M")
        self.assertEqual(True, utils.is_lt(initial, final))