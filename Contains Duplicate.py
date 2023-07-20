#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        newset= set()
        for n in nums:
            if n in newset:
                return True
            newset.add(n)
        return False

