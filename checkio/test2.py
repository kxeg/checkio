#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
# @Author  : xuan

你将得到一个含有整数（X）的非空列表。在这个任务里，你应该返回在此列表中的非唯一元素的列表。要做到这一点，
你需要删除所有独特的元素（这是包含在一个给定的列表只有一次的元素）。解决这个任务时，不能改变列表的顺序。
例如：[1，2，3，1，3] 1和3是非唯一元素，结果将是 [1, 3, 1, 3]。
"""


def checkio(data):
    # Your code here
    # It's main function. Don't remove this function
    # It's used for auto-testing and must return a result for check.
    d = {}
    d1 = {}
    for i in data:
        d[i] = data.count(i)
    for k, v in d.items():
        if v != 1:
            d1.update({k: v})
    L = list(d1.keys())
    data = [i for i in data if i in L]

    # replace this for solution
    return data


# Some hints
# You can use list.count(element) method for counting.
# Create new list with non-unique elements
# Loop over original list


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")