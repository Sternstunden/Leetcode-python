#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#
# https://leetcode.com/problems/multiply-strings/description/
#
# algorithms
# Medium (32.56%)
# Likes:    1444
# Dislikes: 668
# Total Accepted:    257.9K
# Total Submissions: 790K
# Testcase Example:  '"2"\n"3"'
#
# Given two non-negative integers num1 and num2 represented as strings, return
# the product of num1 and num2, also represented as a string.
# 
# Example 1:
# 
# 
# Input: num1 = "2", num2 = "3"
# Output: "6"
# 
# Example 2:
# 
# 
# Input: num1 = "123", num2 = "456"
# Output: "56088"
# 
# 
# Note:
# 
# 
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0
# itself.
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
# 
# 
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ret = [0]*(len(num1)+len(num2))
        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1,-1,-1):
                pos1, pos2 = i+j, i+j+1
                _sum = ret[pos2] + (ord(num1[i])-ord('0')) * (ord(num2[j])-ord('0'))

                ret[pos1] += _sum//10
                ret[pos2] = _sum%10
        
        
        ans = ""
        for i in range(len(ret)):
            if not (len(ans)==0 and ret[i]==0):
                ans += str(ret[i])
        return ans if len(ans)!=0 else "0"
# @lc code=end

