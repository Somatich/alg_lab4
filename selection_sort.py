#!/usr/bin/env python
# -*- coding: utf-8 -*-

def selection_sort(a):
    brd = 0
    mn   = 0
    while brd<len(a):
        mn = brd
        for i in range(brd, len(a)):
            if a[i]<a[mn]:
                mn = i
        a[brd], a[mn] = a[mn], a[brd]
        brd += 1
    return a
