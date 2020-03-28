#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (52.41%)
# Likes:    2568
# Dislikes: 149
# Total Accepted:    491.9K
# Total Submissions: 934.3K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings, group anagrams together.
# 
# Example:
# 
# 
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
# 
# Note:
# 
# 
# All inputs will be in lowercase.
# The order of your output does not matter.
# 
# 
#

# @lc code=start
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_count = {}
        for s in strs:
            count = [0]*26
            for i in s:
                count[ord(i)-ord('a')] += 1
            temp = ''.join(
                [str(i-0) for i in count]
            )
            if temp not in dict_count:
                dict_count[temp] = []
            dict_count[temp].append(s)
        return list(dict_count.values())
# @lc code=end