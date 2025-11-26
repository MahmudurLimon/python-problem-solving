from typing import List
class Solution():
    def max_subarray(self, nums: List[int]) -> List[int]:
        temp_sum = 0
        max_sum = nums[0]
        arr = []
        for i in range(len(nums)):
           if temp_sum < 0:
                temp_sum = 0
                temp_sum = temp_sum + nums[i]
                max_sum = max(max_sum,temp_sum)
                #arr = []
                #arr.append(nums[i])
           else:
                temp_sum = temp_sum + nums[i]
                max_sum = max(max_sum,temp_sum)
                #arr.append(nums[i])
        return max_sum
solution=Solution()
print(solution.max_subarray([-2,-3]))