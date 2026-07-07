import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            a, b = -1 * heapq.heappop(stones), -1 * heapq.heappop(stones)
            if a - b != 0:
                heapq.heappush(stones, b - a)
        return -heapq.heappop(stones) if stones else 0

        """
        scuffed soln
        heapq.heapify_max(stones)
        while len(stones) > 1:
            x, y = heapq.heappop_max(stones), heapq.heappop_max(stones)
            if x == y:
                continue
            heapq.heappush_max(stones, x - y)
        if stones:
            return stones[0]
        else:
            return 0
        """