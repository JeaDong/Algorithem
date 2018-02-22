class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        result = []
        for i in range(1,len(nums)):
            while nums[i] == nums[i-1]:
                result.append(nums[i-1])
                break
        return result