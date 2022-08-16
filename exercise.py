from datetime import timedelta
import my_functions as fc

_file = open('data.txt', 'r')

for i in _file.readlines():
    data = fc.get_data_from_line(i.strip('\n'))
    total = fc.calculate_total_amount(data[1])
    print("The amount to pay %s is: %d USD" % (data[0], total))

_file.close()