from datetime import datetime, timedelta

week_days = ['MO', 'TU', 'WD', 'TH', 'FR']
weekend_days = ['ST', 'SD']

def load_data(filename, my_dict):
    """ Fill my_dict with data

    Parameters:
    filename (string): string for filename (week or weekend)
    """
    try:
        if filename in ['week', 'weekend']:
            _file = open('%s.txt' % filename)
            my_dict[filename] = []
            for i in _file.readlines():
                line_data = i.strip('\n').split(',')
                my_dict[filename].append((line_data[0], line_data[1], int(line_data[2])))
            _file.close()
        else:
            print("Please be sure that the filenames are correct!")
    except:
        print("Be sure if file %s.txt exists!" % filename)


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