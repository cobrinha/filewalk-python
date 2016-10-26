import os
from math import log

class utils(object):
    def __init__(self):
        pass
    
    def sizeof_fmt(self, num):
        unit_list = zip(['bytes', 'kB', 'MB', 'GB', 'TB', 'PB'], [0, 0, 1, 2, 2, 2])
        """Human friendly file size"""
        if num > 1:
            exponent = min(int(log(num, 1024)), len(unit_list) - 1)
            quotient = float(num) / 1024**exponent
            unit, num_decimals = unit_list[exponent]
            format_string = '{:.%sf} {}' % (num_decimals)
            return format_string.format(quotient, unit)
        if num == 0:
            return '0 bytes'
        if num == 1:
            return '1 byte'

    def get_dir_size(self, top):
        total_bytes = 0
        for root, dirs, files in os.walk(top, topdown=False):
            for name in files:
                filename = os.path.join(root, name)
                try:
                    total_bytes += os.path.getsize(filename)
                except:
                    total_bytes += 0
                    pass
                        
            for name in dirs:
                pass
                #print str(os.path.join(root, name))

        return str(total_bytes)
