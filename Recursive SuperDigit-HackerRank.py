#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):    
    def check(n):
        s1=0;
        for i in n:
            s1+=int(i)
        s1=str(s1)
        if len(s1)==1:
            return s1
        else:
            return check(s1)
            
    p=str(check(n)*k)
    return check(p)


# In[3]:


if __name__ == '__main__':
    nk = input().split()
    n = nk[0]
    k = int(nk[1])
    result = superDigit(n, k)
    print(result)


# In[ ]:




