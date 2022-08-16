from datetime import datetime, timedelta

week_days = ['MO', 'TU', 'WD', 'TH', 'FR']
weekend_days = ['ST', 'SD']

my_hours = {  # My hour prices
    "week": [
        ('00:01', '09:00', 25),
        ('09:01', '18:00', 15),
        ('18:01', '00:00', 20),
    ],
    "weekend": [
        ('00:01', '09:00', 30),
        ('09:01', '18:00', 20),
        ('18:01', '00:00', 25),
    ]
}

def get_data_from_line(line):
    """ Return a tuple with (name, days_hours list)

    Parameters:
    line (string): line with formal {name}={list_of_hours_separted_by_comma}
                   ex: ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
    
    Returns: 
    tuple like (name, list_of_string_hours)
    """
    data = line.split("=")
    return (data[0], data[1].split(','))

def parse_time(s):
    """ Return parsed time 

    Parameters:
    s (string): string to parse with format %H:%M

    Returns:
    Datetime: datetime from parsed string
    """
    return datetime.strptime(s, "%H:%M")


def is_between(initial, final, to_check):
    """
    Compare if hour is in a range

    Parameters:
    initial (datetime): range's initial hour
    final (datetime): range's final hour
    to_check (datetime): time to compare

    Returns:
    Boolean: Comparing if time is in range
    """
    return initial <= to_check <= final

def is_lt(initial, final): # is lower than
    """
    Compare if initial is lower than final

    Parameters:
    initial (datetime)
    final (datetime)

    Returns:
    Boleean comparing initial < final
    """
    final = final + timedelta(days=1) if final.hour == 0 and final.minute == 0 else final
    return initial < final

def get_hour_price(day, hour):
    # Return price by hour
    """
    Return hour price by day

    Parameters:
    day (string): two firsts letters of day name
    hour (string): hour string with format %H:%M

    Returns:
    int with data located in my_hours dict
    """
    ranges = my_hours['week'] if day in week_days else my_hours['weekend']
    for _range in ranges:
        initial = parse_time(_range[0])
        final = parse_time(_range[1])
        final = final + timedelta(days=1) if _range[1] == '00:00' else final 
        if is_between(initial, final, hour):
            return _range[2]

def calculate_total_amount(hours_list):
    """
    Calculate total amount based of hours list

    Parameters:
    hour_list (list): List of string with format {DAY}{hour}:{minutes}
                      ex: ['MO10:00-12:00', 'TU10:00-12:00]

    Returns:
    int with total amount calculated
    """
    total = 0
    for i in hours_list:
        day = i[:2]
        _range = i[2:].split("-")
        current_hour = parse_time(_range[0])
        final = parse_time(_range[1])
        while is_lt(current_hour, final):
            total += get_hour_price(day, current_hour)
            current_hour = current_hour + timedelta(hours=1)
    return total