#216. Combination Sum III
'''	Batteries included 
from itertools import combinations

class Solution:
    def combinationSum3(self, k, n):
        return [c for c in combinations(range(1, 10), k) if sum(c) == n]
'''

class Solution:
    def combinationSum3(self, k, target):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        num = [x for x in range(1,10)]
        result = []
        self.com_sum(num,target,0,[],result,k)
        #final = []
        #for i in result:
        #    if len(i) == k:
        #        final.append(i)
        return result
    def com_sum(self,num,target,start,path,result,k):
        
            
        if target < 0:
            return
        if target == 0 and len(path)==k:
            result.append(path)
            return
        
        for i in range(start,9):
            
            if start > 8 or num[i] > target or len(path)>=k:
                break
            self.com_sum(num,target-num[i],i+1,path+[num[i]],result,k)