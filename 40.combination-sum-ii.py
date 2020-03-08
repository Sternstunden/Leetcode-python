#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (45.40%)
# Likes:    1334
# Dislikes: 55
# Total Accepted:    286.2K
# Total Submissions: 628K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate
# numbers sums to target.
# 
# Each number in candidates may only be used once in the combination.
# 
# Note:
# 
# 
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
# [1,2,2],
# [5]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(target,res,index,ret):
            if target == 0:
                ret.append(res)
                return
            for i in range(index,len(candidates)):
                if candidates[i]> target:
                    break
                if i==index or (i>index and candidates[i-1]!=candidates[i]):
                    dfs(target-candidates[i],res+[candidates[i]],i+1,ret)
        ret = []
        candidates.sort()
        dfs(target,[],0,ret)
        return ret
        
# @lc code=end

