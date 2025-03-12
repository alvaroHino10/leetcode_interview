from typing import List, Tuple
from math import prod


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
            Dada una lista de numeros, se debe retornar una lista con el producto de todos los elementos excepto el
            mismo. Este enfoque realiza el producto de todos los elementos removiendo e insertando el elemento actual a
            medida que se recorre la lista, lo cual es ineficiente y no es la mejor solucion.
        :param nums: List[int]: Lista de numeros
        :return: List[int]: Lista con el producto de todos los elementos excepto el mismo
        """
        answer = list(map(lambda x: 1, nums))
        for i in range(len(nums)):
            actual = nums[i]
            nums.remove(actual)
            product = prod(nums)
            answer[i] = product
            nums.insert(i, actual)
        return answer

    def prefix_product(self, nums: List[int]) -> List[int]:
        """
            Calcula el producto de todos los elementos iniciando en izquierda: [1, 2, 3, 4] -> [1, 2, 6, 24]
        :param nums: List[int]: Lista de numeros
        :return: List[int]: Lista con el producto de todos los elementos iniciando en izquierda
        """
        n = len(nums)
        answer = [1] * n
        answer[0] = nums[0]
        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i]
        return answer

    def suffix_product(self, nums: List[int]) -> List[int]:
        """
            Calcula el producto de todos los elementos iniciando en derecha o el final: [1, 2, 3, 4] -> [24, 24, 12, 4]
        :param nums: List[int]: Lista de numeros
        :return: List[int]: Lista con el producto de todos los elementos iniciando en derecha o el final
        """
        n = len(nums)
        answer = [1] * n
        answer[-1] = nums[-1]
        for i in range(1, n):
            answer[n - i - 1] = answer[n - i] * nums[n - i - 1]
        return answer

    def suffix_and_prefix_product(self, nums: List[int]) -> Tuple[List[int], List[int]]:
        """
            Calcula el producto de todos los elementos iniciando en izquierda y derecha o el final.
            Se puede hacer el mismo procedimiento de sufix product y prefix product, pero se hace en un solo paso. Asi
            se evita recorrer la lista dos veces, minimizando el tiempo de ejecucion.
        :param nums: List[int]: Lista de numeros
        :return: Tuple[List[int], List[int]]: Tupla con el producto de todos los elementos prefix y suffix
            respectivamente
        """
        n = len(nums)
        prefix, sufix = [1] * n, [1] * n
        prefix[0] = nums[0]
        sufix[-1] = nums[-1]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i]
            sufix[n - i - 1] = sufix[n - i] * nums[n - i - 1]
        return prefix, sufix

    def product_except_self(self, nums: List[int]) -> List[int]:
        """
            Calcula el producto de todos los elementos excepto el mismo, utilizando el producto de todos los elementos
            obtenidos en prefix y suffix. Para un elemento i, se multiplica el elemento i - 1 de prefix con el elemento
            i + 1 de suffix
        :param nums: List[int]: Lista de numeros
        :return: List[int]: Lista con el producto de todos los elementos excepto el mismo
        """
        prefix, suffix = self.suffix_and_prefix_product(nums)
        n = len(prefix)
        answer = [1] * n
        answer[0] = suffix[1]
        answer[-1] = prefix[n - 2]
        for i in range(1, n - 1):
            answer[i] = prefix[i - 1] * suffix[i + 1]
        return answer

    def product_except_self_internet(self, nums: List[int]) -> List[int]:
        """
            Solucion obtenida de internet, la cual realiza todo el procedimiento en el mismo metodo
        :param nums: List[int]: Lista de numeros
        :return: List[int]: Lista con el producto de todos los elementos excepto el mismo
        """
        n = len(nums)
        left = [1] * n
        right = [1] * n
        answer = [1] * n
        left[0] = nums[0]
        right[-1] = nums[-1]
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i]
            right[n - i - 1] = right[n - i] * nums[n - i - 1]
        answer[0] = right[1]
        answer[n - 1] = left[n - 2]
        for i in range(1, n - 1):
            answer[i] = left[i - 1] * right[i + 1]
        return answer


if __name__ == '__main__':
    s = Solution()
    print(s.suffix_product([1, 2, 3, 4]))  # [24, 12, 8, 6]
    print(s.product_except_self([-1, 1, 0, -3, 3]))  # [0, 0, 9, 0, 0]
