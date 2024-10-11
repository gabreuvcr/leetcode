#https://leetcode.com/problems/reverse-linked-list/

#Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode = next

class Solution:
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        (prev, curr) = (None, head)
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev
