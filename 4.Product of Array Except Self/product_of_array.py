from typing import List

class Solution():
    def product_of_array(self, nums: List[int]) -> List[int]:
        mult = 1
        arr = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i:
                    mult = mult * nums[j]
            arr.append(mult)
            mult = 1
        return arr
solution = Solution()
print(solution.product_of_array([1,2,3,4]))
print(solution.product_of_array([-1,-2,1,5,-6,-3]))