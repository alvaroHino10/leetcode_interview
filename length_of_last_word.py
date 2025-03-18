class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
            Se tiene una cadena de texto s, se debe retornar la longitud de la última palabra en la cadena de texto.
        :param s: str: Cadena de texto
        :return: int: Longitud de la última palabra en la cadena de texto
        """
        word = s.strip().split(' ')
        return len(word[-1])

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord("Hello World")) # 5
    print(s.lengthOfLastWord(" ")) # 0
    print(s.lengthOfLastWord("   fly me   to   the moon  ")) # 4