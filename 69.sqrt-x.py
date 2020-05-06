#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (32.81%)
# Likes:    1113
# Dislikes: 1744
# Total Accepted:    497.2K
# Total Submissions: 1.5M
# Testcase Example:  '4'
#
# Implement int sqrt(int x).
# 
# Compute and return the square root of x, where x is guaranteed to be a
# non-negative integer.
# 
# Since the return type is an integer, the decimal digits are truncated and
# only the integer part of the result is returned.
# 
# Example 1:
# 
# 
# Input: 4
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
# the decimal part is truncated, 2 is returned.
# 
# 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if(x==0):
            return 0
        l, r = 1, x
        while(l<=r):
            mid = l + (r-l)//2
            if(mid > x//mid):
                r = mid - 1
            else:
                l = mid + 1
        return r
# @lc code=end

