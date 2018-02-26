class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()                      
        result = []
        self.combine_sum_2(candidates, 0, [], result, target)
        return result
    def combine_sum_2(self, nums, start, path, result, target):
    
        if not target: #mean sum(path) is equal to target
            result.append(path)
            return

        for i in range(start, len(nums)):
            
            if i > start and nums[i] == nums[i - 1]:
                continue

            
            if nums[i] > target:
                break       #no need to search

           
            self.combine_sum_2(nums, i + 1, path + [nums[i]], 
                               result, target - nums[i])