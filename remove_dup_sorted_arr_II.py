import math
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        actual = nums[0]
        i = 1
        while i < len(nums):
            if actual == nums[i]:
                if count < 2:
                    count += 1
                    i += 1
                else:
                    nums.pop(i)
            else:
                actual = nums[i]
                count = 1
                i += 1
        return len(nums)


if __name__ == "__main__":
    s = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    print(s.removeDuplicates(nums))
    print(nums)
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    print(s.removeDuplicates(nums))
    print(nums)
    nums = [0, 0, 1, 1, 1, 1, 2]
    print(s.removeDuplicates(nums))
    print(nums)
    nums = [1, 2, 3, 3, 3, 4, 4]
    print(s.removeDuplicates(nums))
    print(nums)

