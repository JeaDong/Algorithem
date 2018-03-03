#120. Triangle
'''
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
'''
'''
class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        res = triangle[-1]
        for i in triangle[::-1][1:]:
            for j in range(len(i)):
                res[j] = i[j] + min(res[j],res[j+1])
        return res[0]        
'''
class Solution:
    def minimumTotal(self, triangle):
        f = [0] * (len(triangle) + 1)
        for row in triangle[::-1]:
            for i in range(len(row)):
                f[i] = row[i] + min(f[i], f[i + 1])
        return f[0]