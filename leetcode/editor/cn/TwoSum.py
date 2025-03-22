from typing import *
from leetcode.editor.common.node import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        to_find = target - nums[i]
        # 剩余找
        while i < len(nums):
            for j in nums[i+1:]:
                if to_find == j: return [i, nums.index(j)]
            # 没找到下一个, 直到数组末尾
            i += 1
        return [None,None]
        
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    # your test code here
    nums = [2, 7, 11, 15]
    target = 9
    print(solution.twoSum(nums, target))