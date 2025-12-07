from typing import List

class Solution():
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        arr = []
        sorted_nums = sorted(nums)
        length = len(nums)
        for i in range(length - 2):
            # Skip duplicate values for i
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            left = i + 1
            right = length - 1
            while left < right:
                total = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
                if total == 0:
                    arr.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    # Skip duplicates for left and right
                    while left < right and sorted_nums[left] == sorted_nums[left + 1]:
                        left = left + 1
                    while left < right and sorted_nums[right] == sorted_nums[right - 1]:
                        right = right - 1
                    left = left + 1
                    right = right - 1
                elif total < 0:
                    left = left + 1
                else:
                    right = right - 1
        return arr

solution = Solution()
print(solution.three_sum([-1,0,1,2,-1,-4]))
print(solution.three_sum([-100,-70,-60,110,120,130,160]))