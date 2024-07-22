# https://www.hackerrank.com/challenges/three-month-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here

    n = len(arr)
    plus = 0
    minus = 0
    zero = 0

    for i in arr:
        if i > 0:
            plus += 1
        elif i < 0: 
            minus += 1
        else:
            zero += 1
    
    print(f"{plus/n:.6f}")
    print(f"{minus/n:.6f}")
    print(f"{zero/n:.6f}")


arr = [1,1,0,-1,-1]
plusMinus(arr)

              
