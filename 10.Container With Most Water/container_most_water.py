from typing import List

class Solution():
    def  con_most_water(self, nums: List[int]) -> int:
        min_val = float('-inf')
        index_diff = float('-inf')
        most_water = float('-inf')
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                min_val = min(nums[i],nums[j])
                index_diff = j-i
                water = min_val*index_diff
                if water > most_water:
                    most_water = water
        return most_water
solution = Solution()
print(solution.con_most_water([1,8,6,2,5,4,8,3,7]))
