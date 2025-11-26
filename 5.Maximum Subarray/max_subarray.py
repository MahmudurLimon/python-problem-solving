from typing import List
class Solution():
    def max_subarray(self, nums: List[int]) -> List[int]:
        max_sum = 0
        temp_sum = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                #list[start : end] is a python feature that splits array from start index to before end index (0 -> i-1)
                temp = nums[i:j+1]
                temp_sum = sum(temp)
                if temp_sum > max_sum:
                    max_sum = temp_sum
        return max_sum
solution=Solution()
print(solution.max_subarray([1,3,4,6]))