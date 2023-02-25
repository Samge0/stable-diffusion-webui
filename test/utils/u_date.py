#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/2/23 19:22
# @Author  : Samge
import time


def get_today_str(f='%Y-%m-%d %H:%M:%S') -> str:
    """
    获取当天年月日字符串
    :param f:
    :return:
    """
    return time.strftime(f, time.localtime(time.time()))


def get_timestamp() -> str:
    """
    获取时间戳
    :return:
    """
    return str(int(time.time()))
