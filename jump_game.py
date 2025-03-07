from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
            Se verifica si se puede llegar al final de la lista de números a partir de la posición 0.
        :param nums: List[int] Lista de numeros de salto
        :return: bool: True si se puede llegar al final, False en caso contrario
        """
        # Se recorre la lista desde el final hacia el inicio, se verifica si la suma de la posición actual y el valor en
        # esa posición es mayor o igual a la meta, si es así se actualiza la meta a la posición actual. Al final se
        # verifica si la meta es igual a 0.
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0

if __name__ == '__main__':
    s = Solution()
    print(s.canJump([2,3,1,1,4]))  # True
    print(s.canJump([3,2,1,0,4]))  # False