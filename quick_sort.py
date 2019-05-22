# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 14:45:49 2019

@author: SalnikovPA
"""
#import random 
#import numpy as np
#a = np.array([3,2,1,2,3,4])
lst = [2, 1, 0, -1, -2]
def quick_sort(lst=list(), first=0, last = len(lst)-1):
#    print(a)
#    a = list(a)
#    print('lst', lst)
    print(lst, first, last)
    if first >= last:
        return lst
    else:
        count=0
#        pivpoint = random.randint(first, last-1)
#        pivpoint = first + (last-first)//2
        pivpoint = last
        pvt = lst.pop(pivpoint)
        print('pivpoint', pivpoint)
        j=0
        i=first
        while j < last-first:
            m = lst.pop(i)
            if m<pvt:
                lst.insert(first, m)
                count += 1
                i+=1
            else:
                lst.insert(last-1, m)
                
            j+=1
        print('count', count)
        pivpoint = first + count
        lst.insert(i, pvt)
        return  quick_sort(lst, first, pivpoint-1) and quick_sort(lst, pivpoint+1, last)
print(quick_sort(lst))
            
    