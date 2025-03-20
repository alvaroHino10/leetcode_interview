class Solution:
    def reverseWords(self, s: str) -> str:
        """
            Reverse the words in a string.
        :param s: str: input string
        :return: str: reversed string
        """
        # Method split without params put the words in a list which are separated by space and eliminate the extra
        # spaces
        words = s.strip().split()[::-1]
        return ' '.join(words)
if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords("Let's take LeetCode contest"))
    print(s.reverseWords('  Hello World!  '))
    print(s.reverseWords('a good   example'))