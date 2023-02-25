#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/2/23 19:24
# @Author  : Samge
from test.utils import u_date


def print_log(msg: str) -> None:
    """ 统一打印带有日期信息的日志 """
    print(f'[{u_date.get_today_str()}] {msg}')
