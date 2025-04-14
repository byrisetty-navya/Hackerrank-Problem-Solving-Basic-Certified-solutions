#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'possibleChanges' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY usernames as parameter.
#

def possibleChanges(usernames):
    a=[]
    for i in usernames:
        if(len(i)<=1):
            a.append("NO")
        for j in range(len(i)-1):
            if(i[j]>i[j+1]):
                a.append("YES")
                break
        else:
            a.append("NO")
    return a
        
if _name_ == '_main_':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    usernames_count = int(input().strip())

    usernames = []

    for _ in range(usernames_count):
        usernames_item = input()
        usernames.append(usernames_item)

    result = possibleChanges(usernames)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
