#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (27.25%)
# Likes:    2762
# Dislikes: 119
# Total Accepted:    248.5K
# Total Submissions: 910.6K
# Testcase Example:  '"(()"'
#
# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.
# 
# Example 1:
# 
# 
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# 
# 
# Example 2:
# 
# 
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"
# 
# 
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [(-1,')')]
        ret = 0
        for i, it in enumerate(s):
            if it == ")" and stack[-1][1] == '(':
                stack.pop()
                ret = max(ret, i-stack[-1][0])
            else:
                stack.append((i,it))
        return ret


# @lc code=end

