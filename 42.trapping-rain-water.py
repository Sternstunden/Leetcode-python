#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (46.66%)
# Likes:    5638
# Dislikes: 105
# Total Accepted:    431K
# Total Submissions: 920.8K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it is able to trap after raining.
# 
# 
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In
# this case, 6 units of rain water (blue section) are being trapped. Thanks
# Marcos for contributing this image!
# 
# Example:
# 
# 
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# 
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        """
        水桶问题关键点 -- 短板 
        左右向中间遍历，去最短那边。
        选好一侧后，比较目前与这侧最大值。
        大则取而代之，小则计算在此位置能容纳水量。
        递增或递减。
        """
        l, r = 0, len(height)-1
        res = 0
        max_l, max_r = 0, 0

        while l < r:
            if height[l] <= height[r]:
                if height[l] >= max_l:
                    max_l = height[l]
                else:
                    res += max_l - height[l]
                l += 1
            else:
                if height[r] >= max_r:
                    max_r = height[r]
                else:
                    res += max_r - height[r]
                r -= 1
        return res

# @lc code=end

