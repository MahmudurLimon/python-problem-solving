from typing import List
class Solution():
    def max_prod_subarr(self, nums: List[int]) -> int:
        result = float('-inf')
        curr_tot = 1
        for n in nums:
            curr_tot = curr_tot * n
            print("curt_tot=> ",curr_tot)
            print("result=> ",result)
            if curr_tot > result:
                result = curr_tot
            if curr_tot < 1:
                curr_tot = 1
        return result
solution = Solution()
#print(solution.max_prod_subarr([1,2,-3,4]))
print(solution.max_prod_subarr([-1,-1,-2,3,4,-4]))