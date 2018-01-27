#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
# @Author  : xuan

计算两个日期差的天数
"""

import datetime

def days_diff(date1, date2):
    """
        Find absolute diff in days between dates
    """
    date1 = datetime.date(date1[0], date1[1], date1[2])
    date2 = datetime.date(date2[0], date2[1], date2[2])
    if date2 > date1:
        return (date2-date1).days
    else:
        return (date1-date2).days

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    # assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    # assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    print(days_diff((1982, 4, 19), (1982, 4, 22)))
    print(days_diff((2014, 1, 1), (2014, 8, 27)))
    print(days_diff((2014, 8, 27), (2014, 1, 1)))
