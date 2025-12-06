from typing import List
import random

class Solution():
    def three_sum(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums1 = nums[i+1:]
            nums2 = nums[i+2:]
            sum = nums[i] + nums1[i] + nums2[i]
            print(nums1)
            print(nums2)
            print(sum)
solution = Solution()
print(solution.three_sum([-1,0,1,2,-1,-4]))