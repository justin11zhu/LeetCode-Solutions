#https://leetcode.com/problems/product-of-array-except-self/description/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        size = len(nums) - 1
        for i in range(size):
            prefix[i+1] = prefix[i] * nums[i]
        for i in range(size, 0, -1):
            suffix[i-1] = suffix[i] * nums[i]
        return [suffix[i] * prefix[i] for i in range(size + 1)]

        