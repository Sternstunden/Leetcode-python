#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation/description/
#
# algorithms
# Medium (31.73%)
# Likes:    2695
# Dislikes: 922
# Total Accepted:    317.4K
# Total Submissions: 999.4K
# Testcase Example:  '[1,2,3]'
#
# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
# 
# If such arrangement is not possible, it must rearrange it as the lowest
# possible order (ie, sorted in ascending order).
# 
# The replacement must be in-place and use only constant extra memory.
# 
# Here are some examples. Inputs are in the left-hand column and its
# corresponding outputs are in the right-hand column.
# 
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        先倒序找峰顶，
        若峰顶在队首，直接反转全部
        否则，
        因从峰顶向后都是降序，
        倒序找到大于峰顶前面一位的数字，交换，从而局部形成新的大数，
        但是从峰顶向后还是倒序，
        自峰顶向后进行反转。
        """
        peek = len(nums)-1
        while peek>0 and nums[peek-1]>=nums[peek]:
            peek -= 1
        
        if peek == 0:
            nums.reverse()
            return
        
        head = peek-1
        tail = len(nums)-1
        while nums[tail]<=nums[head]:
            tail -= 1
        
        nums[tail], nums[head] = nums[head], nums[tail]

        l = peek
        r = len(nums)-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

# @lc code=end

