#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
# @Author  : xuan

找到字符串中最长的相同字符重复出现的次数，并返回它的重复次数。
"""
import re

def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    # your code here
    L = []
    p = r'((.)\2{0,9})'
    data = re.findall(p, line)
    for i in data:
        L.append(len(i[0]))

    return max(L,default = 0)

if __name__ == '__main__':
    print(long_repeat("abababaab"))
