import utils
from datetime import timedelta

class Receiver:

    def __init__(self, data):
        self.data = data # filename
        self.my_hours = {}
        utils.load_data('week', self.my_hours)
        utils.load_data('weekend', self.my_hours)

    def get_hour_price(self, day, hour):
        """
        Return hour price by day

        Parameters:
        day (string): two firsts letters of day name
        hour (datetime): hour string with format %H:%M

        Returns:
        int with data located in my_hours dict
        """
        ranges = self.my_hours['week'] if day in utils.week_days else self.my_hours['weekend']
        for _range in ranges:
            initial = utils.parse_time(_range[0])
            final = utils.parse_time(_range[1])
            final = final + timedelta(days=1) if _range[1] == '00:00' else final 
            if utils.is_between(initial, final, hour):
                return _range[2]

    def calculate_total_amount(self, hours_list):
        """
        Calculate total amount based of hours list

        Parameters:
        hour_list (list): List of string with format {DAY}{hour}:{minutes}
                        ex: ['MO10:00-12:00', 'TU10:00-12:00']

        Returns:
        int with total amount calculated
        """
        total = 0
        for i in hours_list:
            day = i[:2]
            _range = i[2:].split("-")
            current_hour = utils.parse_time(_range[0])
            final = utils.parse_time(_range[1])
            while utils.is_lt(current_hour, final):
                total += self.get_hour_price(day, current_hour)
                current_hour = current_hour + timedelta(hours=1)
        return total

    def execute(self):
        _file = open("%s.txt" % self.data, "r")
        for i in _file.readlines():
            data = utils.get_data_from_line(i.strip("\n"))
            total = self.calculate_total_amount(data[1])
            print("The amount to pay %s is: %d USD" % (data[0], total))
        _file.close()
