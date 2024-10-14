#https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = -float('inf')
        total = 0
        for n in range(len(nums)):
            total += nums[n]
            result = max(total, result)
            total = max(0, total)
        return result