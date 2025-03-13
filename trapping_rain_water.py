from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
            Problema de trampa de agua. Se busca calcular la cantidad de agua que se puede almacenar entre las barras o
            extremos, en base a la altura de las barras. Se utiliza el algoritmo de dos punteros para recorrer la lista
            de barras. Solucion inspirada en la explicacion de:
            https://leetcode.com/problems/trapping-rain-water/solutions/5126477/video-keep-max-height-on-the-both-side/
        :param height: List[int]: Lista de alturas de las barras
        :return: int: Cantidad de agua que se puede almacenar
        """
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        water = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
        return water

if __name__ == '__main__':
    s = Solution()
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # 6
    print(s.trap([4,2,0,3,2,5]))  # 9