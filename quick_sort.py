# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 14:45:49 2019

@author: SalnikovPA
"""
#import random 
#import numpy as np
#a = np.array([3,2,1,2,3,4])
lst = [1,-1]
def quick_sort(lst=list(), first=0, last = len(lst)-1):
#    print(a)
#    a = list(a)
#    print('lst', lst)
    print(lst, first, last)
    if first >= last:
        return lst
    else:
        pivpoint = last
        pvt = lst[pivpoint]
        j=0
        i=pivpoint-1
        while j < last-first:
            if lst[i] > pvt:
                lst[i], lst[pivpoint] = lst[pivpoint], lst[i]
                pivpoint-=1
            j+=1
            i-=1
        print(pivpoint)
        return  quick_sort(lst, first, pivpoint-1) and quick_sort(lst, pivpoint+1, last)
print(quick_sort(lst))
            
    