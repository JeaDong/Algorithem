class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
    
        result = ma = 0
        for i,x in enumerate(arr):
            ma = max(ma,x)
            if i == ma:
                result += 1
        return result