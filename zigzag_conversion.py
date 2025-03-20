class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
            Convert the string to zigzag pattern based on the number of rows given as input and return the converted
            word
        :param s: str: Word to convert to zigzag
        :param numRows: int: Number of rows
        :return: str: Zigzag converted word
        """
        matrix = [[''] * len(s) for _ in range(numRows)]
        index_i = 0
        index_j = 0
        step = 0
        if numRows == 1:
            return s
        for i in range(0, len(s)):
            matrix[index_i][index_j] = s[i]
            if index_i == 0:
                step = 1
            elif index_i == numRows - 1:
                step = -1
            if step == -1:
                index_j += 1
            index_i += step
        return ''.join([''.join(row) for row in matrix])

if __name__ == "__main__":
    s = Solution()
    print(s.convert("PAYPALISHIRING", 3)) # Output: "PAHNAPLSIIGYIR"