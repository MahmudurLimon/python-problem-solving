from typing import List

class Solution():
    def max_subarr(self,nums: List[int]) -> List[int]:
        num_len = len(nums)
        n = int((num_len*(num_len+1))/2)
        for i in range(n):
            first_val = nums[i]
            last_val = nums[num_len-1]
            if i >= num_len-1
solution=Solution()
print(solution.max_subarr([1,2,-1,4,-4,2,1]))