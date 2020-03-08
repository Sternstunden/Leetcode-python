#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (25.65%)
# Likes:    5554
# Dislikes: 672
# Total Accepted:    772.5K
# Total Submissions: 3M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
# 
# Note:
# 
# The solution set must not contain duplicate triplets.
# 
# Example:
# 
# 
# Given array nums = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def nSum(l,r,target,n,res,ret):
            if n < 2 or r-l+1<n or nums[l]*n>target or nums[r]*n<target:
                return
            if n == 2:
                while l<r:
                    s = nums[l]+nums[r]
                    if s == target:
                        ret.append(res+[nums[l],nums[r]])
                        l += 1
                        while l<r and nums[l-1] == nums[l]:
                            l += 1
                    elif s<target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(l,r+1):
                    if i == l or (i>l and nums[i-1]!=nums[i]):
                        nSum(i+1,r,target-nums[i],n-1,res+[nums[i]],ret)

        ret = []
        nums.sort()
        nSum(0,len(nums)-1,0,3,[],ret)
        return ret
# @lc code=end

