# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 15:52:05 2019

@author: SalnikovPA
"""

import unittest
import numpy as np
from quick_sort import quick_sort


class TestSelectionSort(unittest.TestCase):
    def test_empty(self):
        a = []
        b = quick_sort(a)
        self.assertTrue(np.array_equal(b, []))

    def test_one(self):
        a = [1]
        b = quick_sort(a)
        self.assertTrue(np.array_equal(b, [1]))

    def test_two(self):
        a = [1, 0]
        b = quick_sort(a)
        self.assertTrue(np.array_equal(b, [0, 1]))

    def test_five(self):
        a = [2, 1, 0, -1, -2]
        b = quick_sort(a)
        self.assertTrue(np.array_equal(b, [-2, -1, 0, 1, 2]))


if __name__ == '__main__':
    unittest.main()
    
#dont know why that is not work
