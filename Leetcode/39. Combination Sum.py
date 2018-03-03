class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []
        self.com_sum(candidates,target,0,[],result)
        return result
    def com_sum(self,candidates,target,start,path,result):
        if target < 0:
            return
        if target == 0:
            result.append(path)
            return
        for i in range(start,len(candidates)):
            if candidates[i] > target:
                break
            self.com_sum(candidates,target-candidates[i],i,path+[candidates[i]],result)
'''
class Solution:
    def combinationSum(self, candidates, target):
        result = []
        candidates = sorted(candidates)
        def dfs(remain, stack):
            if remain == 0:
                result.append(stack)
                return 

            for item in candidates:
                if item > remain: break
                if stack and item < stack[-1]: continue
                else:
                    dfs(remain - item, stack + [item])

        dfs(target, [])
        return result

'''