from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_num = sorted(set(arr))
        rank = {value: rank + 1 for rank, value in enumerate(sorted_num)}
        return [rank[x] for x in arr]


solution = Solution()


print(solution.arrayRankTransform([37,12,28,9,100,56,80,5,12]))