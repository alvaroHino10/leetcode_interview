from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            Se tiene un arreglo de precios de acciones, se debe determinar el máximo beneficio que se puede obtener de
            varias transacciones
        :param prices: List[int] precios de acciones
        :return: int: máximo beneficio
        """
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit

if __name__ == '__main__':
    s = Solution()
    prices = [7,1,5,3,6,4] # 7
    print(s.maxProfit(prices))
    prices = [1,2,3,4,5] # 4
    print(s.maxProfit(prices))