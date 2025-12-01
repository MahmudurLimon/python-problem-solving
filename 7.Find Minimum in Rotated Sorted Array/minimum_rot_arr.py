from typing import List
import random

class Solution():
    def min_rot_arr(self, nums: List[int]) -> int:
        arr_len = len(nums)
        random_num = random.randint(1,arr_len)
        rotated_arr = nums[-random_num:] + nums[:-random_num]
        min = rotated_arr[0]
        for i in range(arr_len):
            if rotated_arr[i] < min:
                min = rotated_arr[i]
        return min
solution = Solution()
print(solution.min_rot_arr([0,1,2,3,4,5]))