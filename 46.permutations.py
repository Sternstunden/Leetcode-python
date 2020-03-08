#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (60.01%)
# Likes:    3062
# Dislikes: 93
# Total Accepted:    515.8K
# Total Submissions: 856.2K
# Testcase Example:  '[1,2,3]'
#
# Given a collection of distinct integers, return all possible permutations.
# 
# Example:
# 
# 
# Input: [1,2,3]
# Output:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
# 
#

# @lc code=start
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums,path:List[int],ret):
            if not nums:
                ret.append(path)
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:],path+[nums[i]],ret)
        ret = []
        dfs(nums,[],ret)
        return ret
# @lc code=end

