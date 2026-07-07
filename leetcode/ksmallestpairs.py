import heapq
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        visited = {}
        pairs = []
        final = []
        # heapq.heapify(pairs)
        heapq.heappush(pairs, (nums1[0]+nums2[0], (0, 0)))

        # ex. pairs = [(3, (1,2)), ()]

        while pairs and len(final) <= k:
            u_idx, v_idx = heapq.heappop(pairs)[1]

            if (u_idx, v_idx) in visited:
                continue
            visited[(u_idx, v_idx)] = True

            u, v = nums1[u_idx], nums2[v_idx]
            final.append((u, v))

            if u_idx + 1 < len(nums1):
                heapq.heappush(pairs, (nums1[u_idx+1] + v, (u_idx + 1, v_idx)))
            if v_idx + 1 < len(nums2):
                heapq.heappush(pairs, (u + nums2[v_idx+1], (u_idx, v_idx + 1)))
                
        return final[:k]