from typing import List

class Solution():
    def contains_duplicate(self,nums: List[int]) -> bool:
        array = []
        for i in range(len(nums)):
            if nums[i] in array:
                return True
            array.append(nums[i])
        return False

solution = Solution()
print(solution.contains_duplicate([44,124,44,765,23]))
