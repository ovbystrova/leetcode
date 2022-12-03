from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time Complexity O(N), Space Complexity O(1)
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head

        _next = head.next.next
        head.val, head.next.val = head.next.val, head.val
        head.next.next = _next

        if head.next.next is not None:
            self.swapPairs(head.next.next)

        return head
