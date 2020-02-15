#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (34.66%)
# Likes:    1999
# Dislikes: 1660
# Total Accepted:    638.7K
# Total Submissions: 1.8M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# Example 1:
# 
# 
# Input: ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# Note:
# 
# All given inputs are in lowercase letters a-z.
# 
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        result = ''
        if n == 0:
            return result

        count = 0
        flag = True
        while flag:
            _temp = None
            for i in strs:
                if count >= len(i):
                    return result
                if not _temp:
                    _temp = i[count]
                elif _temp != i[count]:
                    return result
                if count == len(i)-1:
                    flag = False
            result += _temp
            count += 1
        return result

# @lc code=end

