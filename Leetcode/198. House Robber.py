#198. House Robber
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = cur = 0
        #res = collections.Counter(nums)
        for i in nums:
            prev,cur = cur,max(prev + i,cur)
        return cur