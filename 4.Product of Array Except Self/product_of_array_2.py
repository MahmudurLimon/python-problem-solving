from typing import List

class Solution():
    def product_of_array(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [1] * n
        prefix = 1
        for i in range(n):
            arr[i] = prefix
            prefix = prefix * nums[i]
            print("iloop1=> ",i)
            print("nums1=> ",nums[i])
            print("arr1=> ",arr)
            print("prefix=> ",prefix)
        suffix = 1
        print("----------------------------------")
        for i in range(n-1,-1,-1):
            arr[i] = arr[i] * suffix
            suffix = suffix * nums[i]
            print("iloop2=> ",i)
            print("nums1=> ",nums[i])
            print("arr1=> ",arr)
            print("suffix=> ",suffix)
        return arr
solution = Solution()
print(solution.product_of_array([3,4,5,2]))
#print(solution.product_of_array([-1,-2,1,5,-6,-3]))