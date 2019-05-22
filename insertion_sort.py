#!/usr/bin/env python
# -*- coding: utf-8 -*-

def insertion_sort(a):
    if len(a) == 0:
        return a
    for i in range(1, len(a)):
        stor = a[i]
        for j in range(i-1,-1,-1):
            if a[j] > stor:
                a[j], a[j+1] = a[j+1], a[j]
            else:
#                print(stor)
                break
    return a
