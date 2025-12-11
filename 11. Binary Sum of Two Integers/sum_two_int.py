from typing import List

class Solution():
    def sum_int(self,a,b):
        mask = 0xFFFFFFFF
        sum1 = (a ^ b)
        sum2 = (a & b) << 1
        tot_sum = sum1 + sum2
        print(sum1)
        print(sum2)
        return sum1
solution = Solution()
print(solution.sum_int(2,7))
