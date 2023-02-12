from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0:
            return None

        elif len(lists) == 1:
            return lists[0]

        while len(lists) > 2:
            last = lists.pop(-1)
            lists[-1] = self._merge_two_lists(last, lists[-1])

        return self._merge_two_lists(lists[0], lists[1])


    def _merge_two_lists(self, list1, list2):

        if list1 is None:
            return list2

        elif list2 is None:
            return list1

        if list1.val < list2.val:
            list1.next =  self._merge_two_lists(list1.next, list2)
            return list1

        else:
            list2.next = self._merge_two_lists(list2.next, list1)
            return list2
