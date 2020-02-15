#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.63%)
# Likes:    2847
# Dislikes: 4464
# Total Accepted:    949.8K
# Total Submissions: 3.7M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# 
# Input: 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed
# integer overflows.
# 
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        flag = -1 if x < 0 else 1
        x = abs(x)
        result = 0
        while x:
            result *= 10
            result += x%10
            x //= 10
        result *= flag 
        return result if -2**31<=result<2**31 else 0
# @lc code=end
s = Solution()
print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(120))
