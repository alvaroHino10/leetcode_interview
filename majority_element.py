from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
            Retorna el elemento que aparece más veces en la lista
        :param nums: List[int] Lista de enteros
        :return: int: Elemento que aparece más veces en la lista
        """
        cont = Counter(nums)
        return max(cont, key=cont.get)

if __name__ == "__main__":
    nums = [3, 2, 3]
    s = Solution()
    print(s.majorityElement(nums))
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(s.majorityElement(nums))
    nums = [1]
    print(s.majorityElement(nums))