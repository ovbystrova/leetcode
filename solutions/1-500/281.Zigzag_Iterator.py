from typing import List

class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):

        self.v = []
        self._merge_vectors([v1, v2])
        self.current = -1

        print(self.v)

    def _merge_vectors(self, vectors):

        if len(vectors) > 2:
            vectors = [self._merge_vectors(vectors[:2])] + vectors[2:]

        v1, v2 = vectors[0], vectors[1]

        if len(v1) == 0:
            return self.v.extend(v2)

        elif len(v2) == 0:
            return self.v.extend(v1)

        self.v.append(v1[0])
        self.v.append(v2[0])
        self._merge_vectors([v1[1:], v2[1:]])

    def next(self) -> int:
        self.current += 1
        return self.v[self.current]

    def hasNext(self) -> bool:
        return self.current + 1 < len(self.v)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())