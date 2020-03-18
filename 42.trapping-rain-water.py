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
        l,r = 0, len(height)-1
        res = 0
        ml, mr = 0, 0
        while l<r:
            if height[l] <= height[r]:
                if height[l] >= ml:
                    ml = height[l]
                else:
                    res += ml - height[l]
                l += 1
            else:
                if height[r] >= mr:
                    mr = height[r]
                else:
                    res += mr - height[r]
                r -= 1
        
        return res
# @lc code=end

