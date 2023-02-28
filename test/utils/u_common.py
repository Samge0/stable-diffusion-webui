#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/2/23 19:21
# @Author  : Samge


def str2int(v: str | int) -> int:
    return int(v or 0)


def str2float(v: str) -> float:
    return float(v or 0)
