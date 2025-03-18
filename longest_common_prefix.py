from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
            Se tiene una lista de cadenas de texto, se debe retornar el prefijo común más largo entre todas las cadenas
            de texto.
        :param strs: List[str]: Lista de cadenas de texto
        :return: str: Prefijo común más largo entre todas las cadenas de texto
        """
        # Se realiza un escaneo vertical de las cadenas de texto es decir se compara caracter por caracter de cada
        # cadena
        word = strs[0]
        if len(strs) == 0:
            return ""
        for j in range(len(word)):
            for i in range(1, len(strs)):
                if j == len(strs[i]) or word[j] != strs[i][j]:
                    return word[:j]
        return word

if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))  # "fl"
    print(s.longestCommonPrefix(["dog", "racecar", "car"]))  # ""
    print(s.longestCommonPrefix(["cir", "car"]))  # "c"
    print(s.longestCommonPrefix(['aaa', 'aa', 'aaa']))  # "aa"
