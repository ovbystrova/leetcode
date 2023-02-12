# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self) -> ['NestedInteger']:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):

        self.integers = []
        self._add_items(nestedList)
        self.total = len(self.integers)
        self.current = -1

    def _add_items(self, nestedList):
        for nested_list in nestedList:
            if nested_list.isInteger():
                self.integers.append(nested_list.getInteger())
            else:
                self._add_items(nested_list.getList())

    def next(self) -> int:
        self.current += 1
        return self.integers[self.current]

    def hasNext(self) -> bool:
        return self.current + 1 < self.total

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())