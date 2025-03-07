from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            elif prices[i] - minimum > profit:
                profit = prices[i] - minimum
        return profit

if __name__ == '__main__':
    sol = Solution()
    prices = [7,1,5,3,6,4] # 5
    print(sol.maxProfit(prices))
    prices = [7,6,4,3,1] # 0
    print(sol.maxProfit(prices))
    prices = [2,4,1] # 2
    print(sol.maxProfit(prices))
    prices = [3,2,6,5,0,3] # 4
    print(sol.maxProfit(prices))
    prices = [7,2,1,7,6,4] # 6
    print(sol.maxProfit(prices))
    prices = [7, 2, 3, 7, 6, 4, 1, 8]  # 7
    print(sol.maxProfit(prices))