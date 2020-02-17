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
        n = len(nums)
        result = []
        nums.sort()
        i = 0
        while i<= n-3:
            if nums[i] > 0:
                break
            while 1<=i<=n-3 and nums[i]==nums[i-1]:
                i+=1
            l = i+1
            r = n-1
            while l<r:
                target = nums[l]+nums[r]+nums[i]
                if target == 0:
                    result.append([nums[i],nums[l],nums[r]])
                    l += 1
                    while l<r and nums[l-1] == nums[l]:
                        l+=1
                    r -= 1
                    while l<r and nums[r+1] == nums[r]:
                        r-=1
                elif target < 0:
                    l += 1
                    while l<r and nums[l-1] == nums[l]:
                        l+=1
                else:
                    r -= 1
                    while l<r and nums[r+1] == nums[r]:
                        r-=1
            i += 1
        return result
# @lc code=end

