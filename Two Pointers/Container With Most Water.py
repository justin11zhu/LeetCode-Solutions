#https://leetcode.com/problems/container-with-most-water/description/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        left = 0
        right = len(height) - 1
        while left < right:
            lheight = height[left]
            rheight = height[right]
            area = min(lheight, rheight) * (right - left)
            if area > result:
                result = area
            
            if lheight < rheight:
                left += 1
            else:
                right -= 1
            
        return result
        