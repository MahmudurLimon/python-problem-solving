from typing import List
class Solution():
    def buyAndSell(self, prices: List[int] ) -> int:

        maxProfit = 0
        minPrice = prices[0]
        for i in range(len(prices)):
            minPrice = min(minPrice,prices[i])
            maxProfit = max(maxProfit, prices[i]-minPrice)
        if maxProfit < 0:
            return 0
        else:
            return maxProfit


solution = Solution()
print(solution.buyAndSell([1,2,3,4,2,4,5,3,2]))
print(solution.buyAndSell([5,2,1]))
