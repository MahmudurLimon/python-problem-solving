from typing import List

class Solution():
    def twoSum(self, nums:List[int],target:int) -> List[int]:
        heap = {}
        for i, num in enumerate(nums):
             diff = target - num
             if diff in heap:
                 return [heap[diff],i]
             heap[num] = i

solution = Solution()
print(solution.twoSum([1,2,3,4,5,6], 6))