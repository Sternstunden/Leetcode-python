#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmps = []
        for index in range(len(nums)):
            tmps.append([nums[index], index])
        nums = sorted(tmps)
        left = 0
        right = len(nums)-1
        while left<right:
            if nums[left][0]+nums[right][0] == target:
                return [nums[left][1],nums[right][1]]
            elif nums[left][0]+nums[right][0] > target:
                right -= 1
            else:
                left += 1
        return []
# @lc code=end

