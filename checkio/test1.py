#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
# @Author  : xuan

两个或两个以上的具有相同的频率的字母， 返回那个先出现在字母表中的字母
"""

def checkio(text):
    az = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
    azlist = list(az)
    d = {}
    L2 = []
    text = text.lower()
    for i in text :
        if i.isalpha()==True:
            d[i] = text.count(i)
    L = list(d.values())
    for i in range(len(L)):
        for j in range(i):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
    new_dict = {v:k for k,v in d.items()}
    themax = new_dict.get(L[-1])
    for k,v in d.items():
        if v == d.get(themax):
            L2.append(k)
    #replace this for solution
    if len(L2) > 1:
        for i in range(len(L2)-1):
            for j in range(len(L2)-i-1):
                if azlist.index(L2[j]) > azlist.index(L2[j+1]):
                    L2[j], L2[j + 1] = L2[j + 1], L2[j]
        minz = L2[0]
    else:
        minz = L2[0]
    return minz

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")