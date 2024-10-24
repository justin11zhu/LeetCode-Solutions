#https://leetcode.com/problems/3sum/description/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            if (i > 0) and (nums[i] == nums[i-1]):
                continue
            new_sum = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                cur = nums[left] + new_sum + nums[right]
                if cur > 0:
                    right -= 1
                elif cur < 0:
                    left += 1
                else:                 
                    result.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while right >= 0 and nums[right] == nums[right + 1]:
                        right -= 1
                    while left < len(nums) and nums[left] == nums[left - 1]:
                        left += 1

        return result