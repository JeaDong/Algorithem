						'''暴力解法，遍历所有，O(n^3)'''
class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums or sum(nums)<s:
            return 0
        else:
            n = len(nums)
            final = float('inf')
            for i in range(n):
                for j in range(i,n):
                    result = 0
                    for k in range(i,j+1):
                        result += nums[k]
                    if result >= s:
                        final = min(final,j-i+1)
						break #Found the smallest subarray with sum>=s starting with index i, hence move to next index
            return final
					'''暴力解法，遍历所有，O(n^2)'''
class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums or sum(nums)<s:
            return 0
        else:
            n = len(nums)
            sums = []
            sums.append(nums[0])
            for i in range(1,n):
                sums.append(nums[i]+sums[i-1])
                
            
            final = float('inf')
            for i in range(n):
                for j in range(i,n):
                    result = sums[j] - sums[i] + nums[i]
                    
                    if result >= s:
                        final = min(final,j-i+1)
                        break
            return final
							'''双指针遍历所有，O(n)'''  #原以为要O(n^2),但是从循环改成加减法后优化了时间！！！！
class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums or sum(nums) < s :
            return 0
        else:
            result = float('inf')
            n = len(nums)
            cur = 0
            sums = 0
            for i in range(len(nums)):
                sums += nums[i]
                while sums >= s:
                    result = min(result,i+1-cur)
                    sums -= nums[cur]
                    cur += 1
            return result
                                                    