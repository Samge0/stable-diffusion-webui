#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/2/21 01:37
# @Author  : Samge

from test.utils import u_http


if __name__ == '__main__':
    count = 0
    while True:
        count += 1
        u_http.test_txt2img(count, is_man=True)
