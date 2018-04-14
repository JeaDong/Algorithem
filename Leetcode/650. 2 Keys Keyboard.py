class Solution(object):
    def minSteps(self, n):
        ans = 0
        d = 2
        while n > 1:
            while n % d == 0:
                ans += d
                n /= d
            d += 1
        return ans
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        M = [x for x in range(n+1)]
        
        for i in range(2,n+1):
            for j in range(2,i):
                if i%j == 0:
                    M[i] = min(M[i],M[j]+i//j)
        return M[-1]
                
8
M = [0,1,2,3,4,5,6,7,8]

i = 3, j = 2
i = 4, j = 2  M[4] = min(4,2 + 2) = 4
i = 5, j = 2  
i = 6, j = 2  M[6] = min(6,2+3) = 5
i = 6, j = 3  M[6] = min(5,3+2) = 5
i = 7, j = 2  
i = 8, j = 2  M[8] = min(8,2+4) = 6
i = 8, j = 3
i = 8, j = 4  M[8] = min(6,4+2) = 6
i = 8, j = 5  
...
