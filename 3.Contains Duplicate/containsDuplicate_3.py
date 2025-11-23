#Other solutions from web

from typing import List

class Solution():
    def contains_duplicate(self,nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        else:
            return True

solution = Solution()
print(solution.contains_duplicate([44,124,44,765,23]))
