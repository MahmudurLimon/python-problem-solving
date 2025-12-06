from typing import List
import random

class Solution():
    def search_rot_sort_arr(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        #rand_num = random.randint(1,length)
        #rot_nums = nums[rand_num:] + nums[:rand_num]
        for i in range(length):
            if nums[i] == target:
                return i
        return -1
solution = Solution()
print(solution.search_rot_sort_arr([0,1,2,3,4,5,6],4))
