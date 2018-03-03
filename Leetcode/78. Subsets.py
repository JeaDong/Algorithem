#78. Subsets
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        self.com_sum(nums,0,[],result)
        return result
    
    def com_sum(self,nums,start,path,result):
        if start >= len(nums):
            return
        for i in range(start,len(nums)):
            result.append(path+[nums[i]])
            self.com_sum(nums,i+1,path+[nums[i]],result)