'''
class Solution:
    def findLongestChain(self, pairs):
        cur, res = float('-inf'), 0
        for p in sorted(pairs, key=lambda x: x[1]):
            if cur < p[0]:
                cur, res = p[1], res + 1
        return res'''
class Solution:				#O(n)
    def findLongestChain(self, nums):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        if len(nums)<2:
            return len(nums)
        ans=1
        nums = sorted(nums,key = lambda x:x[1])
        cur = 0
        pur = 1
        while pur <len(nums):
            if nums[cur][-1] < nums[pur][0]:
                ans += 1
                cur = pur
                pur += 1
                continue
            pur += 1
        return ans