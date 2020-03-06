#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
#
# algorithms
# Hard (24.71%)
# Likes:    719
# Dislikes: 1107
# Total Accepted:    161.2K
# Total Submissions: 652.1K
# Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
#
# You are given a string, s, and a list of words, words, that are all of the
# same length. Find all starting indices of substring(s) in s that is a
# concatenation of each word in words exactly once and without any intervening
# characters.
# 
# 
# 
# Example 1:
# 
# 
# Input:
# ⁠ s = "barfoothefoobarman",
# ⁠ words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar"
# respectively.
# The output order does not matter, returning [9,0] is fine too.
# 
# 
# Example 2:
# 
# 
# Input:
# ⁠ s = "wordgoodgoodgoodbestword",
# ⁠ words = ["word","good","best","word"]
# Output: []
# 
# 
#

# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ret = []
        if len(words) == 0:
            return ret          
        d = {}
        for w in words:
            if w in d:
                d[w] += 1
            else:
                d[w] = 1
        l = len(words[0])
        n = len(s)
        count = 0
        for i in range(l):
            subd = {}
            left = i
            count = 0
            for j in range(i,n-l+1,l):
                ww = s[j:j+l]
                if ww in d:
                    if ww in subd:
                        subd[ww] += 1
                    else:
                        subd[ww] = 1
                    count += 1
                    while subd[ww] > d[ww]:
                        subd[s[left:left+l]] -= 1
                        left += l
                        count -= 1
                    if count == len(words):
                        ret.append(left)
                else:
                    subd = {}
                    left = j+l
                    count = 0
        
        return ret 
            

# @lc code=end

