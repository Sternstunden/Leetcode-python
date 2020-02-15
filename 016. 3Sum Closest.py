class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        if len(nums)<3:
            return sum(nums)
        mini = nums[0]+nums[1]+nums[2]
        if mini == target:
            return mini
        else:
            for begin in range(len(nums)-3):
                mid = begin + 1
                end = len(nums)-1
                while mid<end:
                    val = nums[begin]+nums[mid]+nums[end]
                    if abs(val-target)<abs(mini-target):
                        mini = val
                    if val == target:
                        return val
                    elif val < target:
                        mid += 1
                    else:
                        end -=1
        return mini