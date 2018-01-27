#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
# @Author  : xuan
中位数是一个可将数值集合划分为相等的上下两部分的一个数值。
如果列表数据的个数是奇数，则列表中间那个数据就是列表数据的中位数；
如果列表数据的个数是偶数，则列表中间那2个数据的算术平均值就是列表数据的中位数。
在这个任务里，你将得到一个含有自然数的非空数组（X）。你必须把它分成上下两部分，找到中位数。
"""

def checkio(data):
    new_data = sorted(data)
    if len(data) % 2 != 0:
        return new_data[int(len(data)/2)]
    else:
        return (new_data[len(data)//2 -1] + new_data[len(data)//2])/2


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5, "Long."
    print("The local tests are done.")
    print(checkio([1, 2, 3, 4, 5, 6]))