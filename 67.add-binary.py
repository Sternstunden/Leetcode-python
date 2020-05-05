#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (42.12%)
# Likes:    1480
# Dislikes: 255
# Total Accepted:    402.2K
# Total Submissions: 943.3K
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings, return their sum (also a binary string).
# 
# The input strings are both non-empty and contains only characters 1 or 0.
# 
# Example 1:
# 
# 
# Input: a = "11", b = "1"
# Output: "100"
# 
# Example 2:
# 
# 
# Input: a = "1010", b = "1011"
# Output: "10101"
# 
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ret = ''
        carry, _sum = 0, 0
        i, j = len(a)-1, len(b)-1
        while (i>=0 or j>=0):
            _sum = carry
            if(i>=0): _sum += ord(a[i])-ord('0')
            if(j>=0): _sum += ord(b[j])-ord('0')
            carry = _sum//2
            ret = str(_sum%2)+ret
            i -= 1
            j -= 1
        if carry != 0:
            ret = str(carry)+ret
        return ret
# @lc code=end
