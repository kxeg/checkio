#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
# @Author  : xuan

井字游戏判断
"""


def checkio(game_result):
    shu = heng = xie1 = xie2 = False
    for i in range(3):
        if (game_result[0][i] == game_result[1][i] == game_result[2][i]) and \
            game_result[0][i] != ".":
            shu = True
            right = game_result[0][i]

    for j in range(3):
        if game_result[j][0] == game_result[j][1] == game_result[j][2] and \
            game_result[j][0] != ".":
            heng = True
            right1 = game_result[j][0]

    if game_result[0][0] == game_result[1][1] == game_result[2][2] and \
            game_result[0][0] != ".":
        xie1 = True
        right2 = game_result[0][0]

    if game_result[0][2] == game_result[1][1] == game_result[2][0] and \
            game_result[0][2] != ".":
        xie2 = True
        right3 = game_result[0][2]

    if shu:
        return right
    elif heng:
        return right1
    elif xie1:
        return right2
    elif xie2:
        return right3
    else:
        return "D"

if __name__ == "__main__":
    print(checkio([
        "X.O",
        "XX.",
        "XOO"]))
    print(checkio(["OXX",".XX","XOX"]))
    print(checkio(["OOX","X.O","OOX"]))