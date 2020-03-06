#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (33.59%)
# Likes:    3724
# Dislikes: 404
# Total Accepted:    572.1K
# Total Submissions: 1.7M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# 
# You are given a target value to search. If found in the array return its
# index, otherwise return -1.
# 
# You may assume no duplicate exists in the array.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# Example 1:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# 
#

# @lc code=start
import sys
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        l = 0
        r = len(nums)-1
        v_head = nums[0]
        while l<=r:
            mid = (l+r)//2
            
            v_mid = nums[mid]
            if (target<v_head) != (v_mid<v_head):
                v_mid = -sys.maxsize if target<v_head else sys.maxsize

            if v_mid < target:
                l = mid+1
            elif v_mid > target:
                r = mid-1
            else:
                return mid
        return -1

# @lc code=end

