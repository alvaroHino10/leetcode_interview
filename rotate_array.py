from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> List[int]:
        """
            Se tiene un arreglo de enteros, se debe rotar el arreglo k veces.
        :param nums: List[int]: Lista de enteros
        :param k: int: Número de rotaciones
        :return: Lista de enteros rotada k veces
        """
        # Se aplica el modulo para cuando k es un numero mayor a la longitud de la lista y asi obtener la cantidad de
        # rotaciones equivalentes a k
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        return nums

if __name__ == '__main__':
    s = Solution()
    print(s.rotate([1, 2, 3, 4, 5, 6, 7], 3))  # [5, 6, 7, 1, 2, 3, 4]
    print(s.rotate([-1, -100, 3, 99], 2))  # [3, 99, -1, -100]
    print(s.rotate([1, 2], 3))  # [2, 1]