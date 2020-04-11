#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
# https://leetcode.com/problems/jump-game-ii/description/
#
# algorithms
# Hard (29.64%)
# Likes:    1900
# Dislikes: 112
# Total Accepted:    224.4K
# Total Submissions: 755.5K
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
# 
# Each element in the array represents your maximum jump length at that
# position.
# 
# Your goal is to reach the last index in the minimum number of jumps.
# 
# Example:
# 
# 
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
# ⁠   Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# Note:
# 
# You can assume that you can always reach the last index.
# 
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        _max = 0
        _end = 0
        count = 0
        for i, item in enumerate(nums):
            if _end == len(nums)-1:
                break

            _max = max(_max, i+item)
            
            if i == _end:
                count += 1
                _end = _max

        return count
# @lc code=end

