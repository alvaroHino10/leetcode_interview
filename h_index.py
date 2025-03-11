from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
            Se tiene un arreglo de citas de un autor, se quiere saber el h-index del autor. El h-index es el mayor
            número h tal que el autor tiene al menos h citas en h de sus trabajos.
        :param citations: List[int]: Arreglo de citas de un autor
        :return: int: h-index del autor
        """
        citations.sort(reverse=True)
        if len(citations) == 1:
            return 1 if citations[0] > 0 else 0
        for i in range(len(citations)):
            if i >= citations[i]:
                return i
        i = len(citations)
        return i

if __name__ == "__main__":
    citations = [3, 0, 6, 1, 5]
    print(Solution().hIndex(citations))  # 3
    citations = [1, 3, 1]
    print(Solution().hIndex(citations))  # 1
    citations = [100]
    print(Solution().hIndex(citations))  # 1
    citations = [0]
    print(Solution().hIndex(citations))  # 0
    citations = [0, 0]
    print(Solution().hIndex(citations))  # 0
    citations = [1]
    print(Solution().hIndex(citations))  # 1
    citations = [11,15]
    print(Solution().hIndex(citations))  # 1
