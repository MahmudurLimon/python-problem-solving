from typing import List

class Solution():
    def con_most_water(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_water_area = 0
        while left < right:
            min_val = min(height[left],height[right])
            diff = right - left
            water_area = min_val*diff
            max_water_area = max(max_water_area,water_area)
            if height[left] < height[right]:
                left = left + 1
            else:
                right -= 1
        return max_water_area
solution = Solution()
print(solution.con_most_water([1,8,6,2,5,4,8,3,7]))
