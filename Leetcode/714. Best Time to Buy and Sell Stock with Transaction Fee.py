#714. Best Time to Buy and Sell Stock with Transaction Fee
# O(n) time, O(1) space   Greedy
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        buy = prices[0]
        res = 0
        for p in prices:
            if buy > p: # current price is less than last buy
                buy = p # buy at p
            else:
                tmp = p - buy - fee
                if tmp > 0: # have profit
                    res += tmp
                    buy = p - fee #I am confusing about this!
        return res
		
714. Best Time to Buy and Sell Stock with Transaction Fee