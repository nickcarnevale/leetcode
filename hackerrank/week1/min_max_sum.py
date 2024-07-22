#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    a = sorted(arr)
    
    minimum = a[0] + a[1] + a[2] + a[3]
    maximum = a[1] + a[2] + a[3] + a[4]
    
    print(minimum, maximum)


def miniMaxSum2(arr):
    # Write your code here
    a = sorted(arr)
    n = len(a)
    
    minimum = 0
    maximum = 0
    
    for i in range(1,n):
        minimum += a[i-1]
        maximum += a[i]
        
    print(minimum, maximum)