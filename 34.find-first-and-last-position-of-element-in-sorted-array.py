#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (35.00%)
# Likes:    2558
# Dislikes: 116
# Total Accepted:    417.9K
# Total Submissions: 1.2M
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in ascending order, find the starting
# and ending position of a given target value.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# If the target is not found in the array, return [-1, -1].
# 
# Example 1:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# 
# Example 2:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# 
#

# @lc code=start
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ret = [-1,-1]
        if not nums:
            return ret

        l = 0
        r = len(nums)-1
        while l<r:
            mid = l+(r-l)//2
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid
        if nums[l] != target:
            return ret
        r = len(nums)-1
        ll = l
        while l<r:
            mid = l+(r-l)//2+1
            if nums[mid] > target:
                r = mid-1
            else:
                l = mid
        return [ll,r]
        

# @lc code=end

