from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
            Se calcula el número mínimo de saltos necesarios para llegar al final de la lista de números a partir
            de la posición 0. Se inicia salto en 1 porque se asume el primer salto y se inicia en  i=1.
        :param nums: List[int] Lista de números de salto
        :return: int: Número mínimo de saltos necesarios para llegar al final
        """
        if len(nums) <= 1:
            return 0
        jumps = 1
        max_jump = nums[0]
        new_end = nums[0]
        for i in range(1, len(nums) - 1):
            max_jump = max(max_jump, i + nums[i])
            if i == new_end:
                jumps += 1
                new_end = max_jump
                if new_end >= len(nums) - 1:
                    break
        return jumps


if __name__ == '__main__':
    s = Solution()
    print(s.jump([2, 3, 1, 1, 4]))  # 2
    print(s.jump([2, 3, 0, 1, 4]))  # 2
    print(s.jump([2, 3, 1, 1, 4]))  # 2
    print(s.jump([1, 1, 1, 1, 4]))  # 4
    print(s.jump([1, 2, 1, 1, 1]))  # 3
