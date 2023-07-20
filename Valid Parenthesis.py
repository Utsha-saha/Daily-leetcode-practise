#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        bracketClose={")":"(","}":"{","]":"["}

        for c in s:
            if c in bracketClose:
                if stack and stack[-1]==bracketClose[c]:
                    stack.pop()
                else:
                    return False

            else: 
                stack.append(c)
        return True if not stack else False


# In[ ]:




