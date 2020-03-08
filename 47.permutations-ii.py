#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (44.03%)
# Likes:    1557
# Dislikes: 56
# Total Accepted:    311.2K
# Total Submissions: 704.5K
# Testcase Example:  '[1,1,2]'
#
# Given a collection of numbers that might contain duplicates, return all
# possible unique permutations.
# 
# Example:
# 
# 
# Input: [1,1,2]
# Output:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums,path:List[int],ret):
            if not nums:
                ret.append(path)
            for i in range(len(nums)):
                if i == 0 or ( i>0 and nums[i-1]!=nums[i]):
                    dfs(nums[:i]+nums[i+1:],path+[nums[i]],ret)
        ret = []
        nums.sort()
        dfs(nums,[],ret)
        return ret
# @lc code=end

