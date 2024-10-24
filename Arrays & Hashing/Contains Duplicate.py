#https://leetcode.com/problems/contains-duplicate/submissions/1284499850/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for i in nums:
            before = len(nums_set)
            nums_set.add(i)
            if len(nums_set) == before:
                return True
        return False