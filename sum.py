#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: sum.py

n = 100
sum = 0
counter = 1
while counter <= n:
    sum += counter
    counter += 1

print('Sum of 1 until %d: %d' % (n, sum))
