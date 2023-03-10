from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # visited = set()

        # while head is not None and head.next is not None:
        #     if head in visited:
        #         return head
        #     visited.add(head)
        #     head = head.next

        # return None

        while head is not None and head.next is not None:
            if head.val == "done":
                return head

            head.val = "done"
            head = head.next

        return None
