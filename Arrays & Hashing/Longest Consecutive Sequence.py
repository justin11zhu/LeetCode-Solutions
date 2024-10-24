#https://leetcode.com/problems/longest-consecutive-sequence/submissions/
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_set = set(nums)
        result = 0
        for n in nums:
            before = len(my_set)
            my_set.discard(n-1)
            after = len(my_set)
            if before == after:
                size = 1
                restart = True
                while restart:
                    before = len(my_set)
                    n+=1
                    my_set.discard(n)
                    after = len(my_set)
                    if before == after:
                        if size > result:
                            result = size
                        restart = False
                    size += 1
            else:
                my_set.add(n-1)

 
        return result