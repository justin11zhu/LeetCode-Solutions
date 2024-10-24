#https://leetcode.com/problems/jump-game-ii/description/
class Solution:
    def jump(self, nums: List[int]) -> int:
        result = 0
        head = 0
        tail = 0
        steps = nums[head]

        while tail < len(nums) - 1:
            for i in range(steps):
                steps -= 1
                tail += 1
                if tail >= len(nums):
                    break
                steps = max(steps, nums[tail])

            head = tail
            result += 1

        return result
