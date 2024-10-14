#https://leetcode.com/problems/jump-game/
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        steps = nums[0]
        pos = 0
        while steps >= 0:
            if pos == len(nums)-1:
                return True
            steps = max(steps, nums[pos])
            pos += 1
            steps -= 1
            
        return False