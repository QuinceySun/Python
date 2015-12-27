#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: recur_fibo.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-28 00:41:49
############################

def recur_fibo(n):
    '''递归函数
    输出斐波那契数列'''
    if n <= 1:
        return n
    else:
        return(recur_fibo(n - 1) + recur_fibo(n - 2))

# 获取用户输入
nterms = int(input('您要输出几项？ '))

# 检查输入的数字是否正确
if nterms <= 0:
    print('请输入正数')
else:
    print('斐波那契数列： ')
    for i in range(nterms):
        print(recur_fibo(i))
