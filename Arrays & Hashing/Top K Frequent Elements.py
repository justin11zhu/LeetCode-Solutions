#https://leetcode.com/problems/top-k-frequent-elements/description/
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        "first pass"
        count = {}
        buckets = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for key, value in count.items():
            buckets[value].append(key)
        result = []
        for i in range(len(buckets)-1, 0, -1):
            for j in buckets[i]:
                result.append(j)
                if len(result) == k:
                    return result        