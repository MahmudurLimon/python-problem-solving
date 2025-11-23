from typing import List

class Solution():
    def contains_duplicate(self,nums: List[int]) -> bool:
        heap = {}

        for i, val in  enumerate(nums):
            print("i: ",i)
            print("val: ",val)
            print("nums: ",nums)
            print("nums[i]: ",nums[i])
            if val in heap:
                return True
            heap[val] = i
            print("heap[val]: ",heap[val])
            print("heap: ",heap)

        return False

solution = Solution()
print(solution.contains_duplicate([44,124,44,765,23]))
