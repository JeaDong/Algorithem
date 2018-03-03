#48. Rotate Image
'''
class Solution:
    def rotate(self, A):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        A[:] = zip(*A[::-1])
'''

'''
 A[:] = [[row[i] for row in A[::-1]] for i in range(len(A))]
'''

'''  rude solution
n = len(A)
        for i in range(n//2):
            for j in range(n-n//2):
                A[i][j], A[~j][i], A[~i][~j], A[j][~i] = \
                         A[~j][i], A[~i][~j], A[j][~i], A[i][j]
'''
		
