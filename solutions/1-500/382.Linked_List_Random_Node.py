import random
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head


    def getRandom(self) -> int:

        current_id = 1
        head = self.head
        value = head.val

        while head.next is not None:
            current_id += 1
            head = head.next
            prob = random.random()

            if prob < 1 / current_id:
                value = head.val

        return value

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()