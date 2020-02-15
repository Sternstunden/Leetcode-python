#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        
        # dp[i][j] means whether s(i, j) is palindromic
        dp = [[False for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = True
        
        start, maxLen = 0, 1
        for l in range(n - 1, -1, -1):
            for length in range(2, n - l + 1):
                r = l + length - 1
                dp[l][r] = s[l] == s[r] and (r == l + 1 or dp[l + 1][r - 1])
                if dp[l][r] and length > maxLen:
                    start, maxLen = l, length
                    
        end = start + maxLen
        return s[start:end]
# @lc code=end
