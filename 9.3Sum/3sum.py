from typing import List
import random

class Solution():
    def three_sum(self, nums: List[int]) -> List[int]:
        arr = []
        sorted_nums = sorted(nums)
        length = len(nums)
        for i in range(length):
            for j in range(length-1):
                sum = sorted_nums[i] + sorted_nums[j] + sorted_nums[j+1]
                if sum == 0:
                    triplet = [sorted_nums[i],sorted_nums[j],sorted_nums[j+1]]
                    sorted_triplet = sorted(triplet)
                    if sorted_triplet not in arr:
                        arr.append(sorted_triplet)
        return arr
solution = Solution()
print(solution.three_sum([-1,0,1,2,-1,-4]))
print(solution.three_sum([-100,-70,-60,110,120,130,160]))
