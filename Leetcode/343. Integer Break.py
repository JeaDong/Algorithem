class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2: return 1
        if n == 3: return 2
        x = n//3
        y = n%3
        result = [3 for x in range(x)]
        if y == 1:
            result[-1] += 1
        if y == 2:
            result.append(2)
        fina = 1
        for i in result:
            fina = fina * i
        return fina