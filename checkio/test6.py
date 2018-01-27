#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
# @Author  : xuan

写出一个max和min函数，可选的唯一关键字用于从每个列表中中提取一个用于比较的参数的函数
"""


def min(*args, **kwargs):
    key = kwargs.get("key", lambda x: x)
    if len(args) == 1:
        values = args[0]
    else:
        values = args

    min_value = next(iter(values))
    for value in values:
        if key(value) < key(min_value):
            min_value = value
    return min_value


def max(*args, **kwargs):
    key = kwargs.get("key", lambda x: x)
    if len(args) == 1:
        values = args[0]
    else:
        values = args

    max_value = next(iter(values))
    for value in values:
        if key(value) > key(max_value):
            max_value = value
    return max_value



if __name__ == "__main__":
    print(max([1,2],key=lambda x: x*2))
    print(max([1],key = lambda x:x*x))
    print(max("hello"))
    print(max(2.2, 5.6, 5.9,key = int))
    print(max([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]))