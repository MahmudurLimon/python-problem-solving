from typing import List
class Solution():
    def max_prod_subarr(self, nums: List[int]) -> int:
        result = float('-inf')
        curr_tot = 1
        check_val = nums[0]
        if check_val < 0:
            bool = 0
        else:
            bool = 1
        for n in nums:
            if n < 0:
                if bool == 0:
                    curr_tot = curr_tot * n
                    print("curt_tot=> ",curr_tot)
                    print("result=> ",result)
                    if curr_tot > result:
                        result = curr_tot
                    if curr_tot == 0:
                        curr_tot = 1
                    bool = 0
            elif n > 0:
                if bool == 1:
                    curr_tot = curr_tot * n
                    print("curt_tot=> ",curr_tot)
                    print("result=> ",result)
                    if curr_tot > result:
                        result = curr_tot
                    if curr_tot < 1:
                        curr_tot = 1
                    bool = 1
        return result
solution = Solution()
print(solution.max_prod_subarr([1,2,-3,4]))
print(solution.max_prod_subarr([-1,-1,-2,3,4,-4]))