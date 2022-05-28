from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Recursive Solution: Time Compexity O(n), Space Complexity O(1)
class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        node = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return node
