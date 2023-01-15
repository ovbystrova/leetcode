from collections import defaultdict
from typing import List

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple:List[bool]) -> int:

        vertice_map = defaultdict(list)
        for s, e in edges:
            vertice_map[s].append(e)
            vertice_map[e].append(s)

        time = self.dfs(
            vertice=0,
            parent=-1,
            vertice_map=vertice_map,
            hasApple=hasApple
        )
        return max(time - 2, 0)  # -2 because we start from 0 already

    def dfs(self, vertice, parent, vertice_map, hasApple):

        total_time = 0

        for child in vertice_map[vertice]:
            if child != parent:
                total_time += self.dfs(
                    vertice=child,
                    parent=vertice,
                    vertice_map=vertice_map,
                    hasApple=hasApple

                )
        if total_time > 0 or hasApple[vertice]:
            return total_time + 2

        return total_time
