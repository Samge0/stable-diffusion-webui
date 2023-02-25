#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/2/23 21:48
# @Author  : Samge
import re


def initial_capital(v: str) -> str:
    """将句子 首字母跟空格后面的字母 转大写"""
    result = ''
    for i in range(len(v)):
        if i == 0:
            result += v[0].upper()
        elif v[i - 1] == ' ':
            result += v[i].upper()
        else:
            result += v[i]
    return result


def keep_chinese_alphanumeric(v: str) -> str:
    """ 移除空格等字符，只保留字母汉字数字"""
    return '' if not v else ''.join(re.findall(r'[A-Za-z0-9\u4e00-\u9fa5]', v))


if __name__ == '__main__':
    print(keep_chinese_alphanumeric('dsd#*……&（6lsdjsk第三课时djsdkdn洒水多2饿78sd'))
    print(initial_capital('the sun setting over the ocean'))
