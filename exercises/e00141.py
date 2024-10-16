#https://leetcode.com/problems/linked-list-cycle/

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: Optional[ListNode] = None

class Solution:
    def has_cycle(self, head: Optional[ListNode]) -> bool:
        slower, faster = head, head

        while slower and faster and faster.next:
            slower = slower.next
            faster = faster.next.next

            if slower == faster:
                return True
            
        return False
