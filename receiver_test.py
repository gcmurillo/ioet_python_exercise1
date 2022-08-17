import unittest
import receiver
import datetime

class ReceiverTests(unittest.TestCase):
    def setUp(self):
        self.receiver = receiver.Receiver('data')

    def test_get_hour_price(self):
        hour = datetime.datetime.strptime("01:00", "%H:%M")
        self.assertEqual(25, self.receiver.get_hour_price('MO', hour))

    def test_calculate_total_amount(self):
        self.assertEqual(self.receiver.calculate_total_amount(['MO10:00-12:00', 'TU10:00-12:00']), 60)