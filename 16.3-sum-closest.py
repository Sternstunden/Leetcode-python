#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (45.72%)
# Likes:    1622
# Dislikes: 117
# Total Accepted:    421.4K
# Total Submissions: 921.9K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.
# 
# Example:
# 
# 
# Given array nums = [-1, 2, 1, -4], and target = 1.
# 
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
# 
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n<=3:
            return sum(nums)
        nums.sort()
        temp = nums[0]+nums[1]+nums[2]
        i = 0
        while i<=n-3:
            l = i+1
            r = n-1
            while l<r:
                ret = nums[i]+nums[l]+nums[r]
                if abs(target-ret)<abs(target-temp):
                    temp = ret
                if target - ret == 0:
                    return ret
                elif target>ret:
                    l += 1
                    while l<r and nums[l-1] == nums[l]:
                        l+=1
                else:
                    r -= 1
                    while l<r and nums[r+1] == nums[r]:
                        r-=1
            i += 1
        return temp
# @lc code=end
