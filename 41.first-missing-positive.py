#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#
# https://leetcode.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (30.70%)
# Likes:    2632
# Dislikes: 715
# Total Accepted:    285.3K
# Total Submissions: 927.7K
# Testcase Example:  '[1,2,0]'
#
# Given an unsorted integer array, find the smallest missing positive integer.
# 
# Example 1:
# 
# 
# Input: [1,2,0]
# Output: 3
# 
# 
# Example 2:
# 
# 
# Input: [3,4,-1,1]
# Output: 2
# 
# 
# Example 3:
# 
# 
# Input: [7,8,9,11,12]
# Output: 1
# 
# 
# Note:
# 
# Your algorithm should run in O(n) time and uses constant extra space.
# 
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''
        1. 第一个正数绝对存在 [1,l+1]区间
        2. n = l+1 , 利用index mod n 作为hash方式,统计数值出现次数。
        '''
        nums += [0]
        n = len(nums)
        for i in range(n):
            if nums[i]<0 or nums[i]>=n:
                nums[i] = 0

        for i in range(n):
            nums[nums[i]%n] += n
        
        for i in range(1,n):
            if nums[i]//n == 0:
                return i
        return n

# @lc code=end

