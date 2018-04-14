#647. Palindromic Substrings
'''								984ms
class Solution:
    def countSubstrings(self, nums):
        """
        :type s: str
        :rtype: int
        """
        #nums = [i for i in nums]
        cur = 0
        result = []
        e = len(nums) 
        for i in range(1,e+1):
            while i <= e:
                if nums[cur:i] == nums[cur:i][::-1]:
                    result.append(nums[cur:i])
                i += 1
            cur += 1
        return len(result)
'''	
'''								800ms
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    res += 1
        return res
'''
'''								120ms
class Solution:
    def countSubstrings(self, S):
        N = len(S)
        ans = 0
        for center in range(2*N - 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < N and S[left] == S[right]:
                ans += 1
                left -= 1
                right += 1
        return ans
'''
''' Use two pointer to find a consecutive substring with the same char, sum them up and add it to result, then start looking to the left and to the right. 44ms
def countSubstrings(self, s):
    """
    :type s: str
    :rtype: int
    """
    ret = 0
    left, right = 0, 0
    while left < len(s):
        while right < len(s) and s[right] == s[left]:
            right += 1
        ret += self.sum(right - left)
        l, r = left-1, right
        while l >= 0 and r < len(s) and s[r] == s[l]:
            ret += 1
            l -= 1
            r += 1
        left = right
    return ret
            
def sum(self, n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s
'''
'''						776 ms
class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum(s[i:j] == s[i:j][::-1] for j in range(len(s) + 1) for i in range(j))
'''
'''					52 ms
class Solution:
    def countSubstrings(self, S):
        def manachers(S):
            A = '@#' + '#'.join(S) + '#$'
            Z = [0] * len(A)
            center = right = 0
            for i in range(1, len(A) - 1):
                if i < right:
                    Z[i] = min(right - i, Z[2 * center - i])
                while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
                    Z[i] += 1
                if i + Z[i] > right:
                    center, right = i, i + Z[i]
            return Z

        return sum((v+1)//2 for v in manachers(S))
'''