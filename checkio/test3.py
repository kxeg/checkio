#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
# @Author  : xuan
密码安全检查模块。如果密码的长度大于或等于10个符号，
至少有一个数字，一个大写字母和一个小写字母，该密码将被视为足够强大
"""

def checkio(data):
    passk = False
    nums = low = upp = 0
    if len(data)>=10:
        for i in data:
            if i.isalpha() or i.isdigit():
                if i.isdigit():
                    nums +=1
                if i.islower():
                    low += 1
                if i.isupper():
                    upp += 1
    if nums >= 1 and low>=1 and upp >= 1:
        passk = True
    #replace this for solution
    return passk

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
