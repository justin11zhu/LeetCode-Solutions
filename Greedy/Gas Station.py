#https://leetcode.com/problems/gas-station/
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start = 0
        result = 0
        total = 0
        while start < len(gas):
            total += gas[start] - cost[start]
            start += 1
            if total < 0:
                result = start
                total = 0

        return result
    