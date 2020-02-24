#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#
# https://leetcode.com/problems/divide-two-integers/description/
#
# algorithms
# Medium (16.19%)
# Likes:    921
# Dislikes: 4482
# Total Accepted:    243.9K
# Total Submissions: 1.5M
# Testcase Example:  '10\n3'
#
# Given two integers dividend and divisor, divide two integers without using
# multiplication, division and mod operator.
# 
# Return the quotient after dividing dividend by divisor.
# 
# The integer division should truncate toward zero.
# 
# Example 1:
# 
# 
# Input: dividend = 10, divisor = 3
# Output: 3
# 
# Example 2:
# 
# 
# Input: dividend = 7, divisor = -3
# Output: -2
# 
# Note:
# 
# 
# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 2^31 − 1 when the division
# result overflows.
# 
# 
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        flag = 1
        if (dividend<0 and divisor>0) or (dividend>0 and divisor<0):   
            flag = -1
        dividend, divisor = abs(dividend), abs(divisor)
        ret = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend>=temp:
                dividend -= temp
                ret += i
                i <<= 1
                temp <<= 1
        ret  *= flag
        return max(min(2**31-1,ret),-2**31)
# @lc code=end
