#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (59.54%)
# Likes:    4074
# Dislikes: 228
# Total Accepted:    466.1K
# Total Submissions: 781.6K
# Testcase Example:  '3'
#
# 
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# 
# For example, given n = 3, a solution set is:
# 
# 
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
# 
#

# @lc code=start
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(s,l,r,n):
            if l+r == 2*n:
                ret.append(s)
                return
            if l<n:
                generate(s+'(',l+1,r,n)
            if l>r:
                generate(s+')',l,r+1,n)
        
        ret = []
        generate('',0,0,n)
        return ret
# @lc code=end
print (Solution().generateParenthesis(3))
