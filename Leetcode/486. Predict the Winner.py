class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def dp(nums,p1,p2,turn):
            if not nums:
                return p1 >= p2
            if turn:
                return dp(nums[1:],p1,p2+nums[0],0) and dp(nums[:-1],p1,p2+nums[-1],0)
            return dp(nums[1:],p1+nums[0],p2,1) or dp(nums[:-1],p1+nums[-1],p2,1)
        return dp(nums,0,0,0)

class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)%2 == 0 or len(nums) == 1:
            return True

        n = len(nums)
        dp = [[[0,0] for row in xrange(n)] for _ in xrange(n)]
        
        # bottom up, build each case starting from problem with 1 number in a game:
        # base case: only 1 number, player 1 pick first, player 2 will be left with 0 number game, aka 0
        # each dp[i][j] will store [bestScore, leftOver]
        for i in range(n):
            dp[i][i] = [nums[i], 0]
        
        # sub divide the game into list from index i to j 
        # now start from 2 number game [i][j]:
        # if player 1 pick i, player 2 will pick the bestScore of game [i+1][j], then player 1 is left with the leftOver of game [i+1][j]
        # if player 1 pick j, player 2 will pick the bestScore of game [i][j-1], then player 1 is left with the leftOver of game [i][j-1]
        # player 1 will choose the best case in above scenarios

        for length in xrange(2,n+1):
            for i in range(n-length+1):
                j = i + length-1
                # pick i:
                pi = dp[i+1][j][1] + nums[i]
                # pick j:
                pj = dp[i][j-1][1] + nums[j]
                if pi > pj:
                    dp[i][j][0] = pi
                    dp[i][j][1] = dp[i+1][j][0]

                else:
                    dp[i][j][0] = pj
                    dp[i][j][1] = dp[i][j-1][0]

        return dp[0][-1][0] >= dp[0][-1][1]
class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        # initialize a n*n*2 matrix, dp[i][k][0] means 
        # for beginning array nums[i:k+1], player1's score, 
        # and dp[i][k][1] means player2's.
        dp = [[[0 for state in range(2)] for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i][0] = nums[i]
        for i in range(1, n):
            #internal from 1 to n-1
            for k in range(n-i):
                # two strategies of player1
                p1_1 = nums[k]+dp[k+1][k+i][1]
                p1_2 = nums[k+i]+dp[k][k+i-1][1]
                if p1_1 > p1_2:
                    dp[k][k+i][0] = p1_1
                    dp[k][k+i][0] = p1_1
                    dp[k][k+i][1] = dp[k+1][k+i][0]
                else:
                    dp[k][k+i][0] = p1_2
                    dp[k][k+i][1] = dp[k][k+i-1][0]
        # player1 win the game if the got the same scores.
        return dp[0][n-1][0] >= dp[0][n-1][1]