# -*- encoding : utf-8 -*-
"""
@File       : prog.py
@Time       :2020/9/9 16:29
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
import argparse
import sys


parser = argparse.ArgumentParser(description='Process some Integers.')

parser.add_argument('--first', '-f', required=True)

parser.add_argument('--second', '-s', required=True)

args = parser.parse_args(sys.argv[1:])


def deal(conf):
    first = conf.first
    second = conf.second
    print(first, second)


deal(args)
