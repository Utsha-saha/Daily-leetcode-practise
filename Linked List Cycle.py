#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ptr1,ptr2=head,head
        
        while ptr2 and ptr2.next:
            ptr1=ptr1.next
            ptr2=ptr2.next.next
            if ptr1==ptr2:
                return True
        return False

