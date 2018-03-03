#338. Counting Bits
'''
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        nums = [x for x in range(num+1)]
        bnum = [bin(x) for x in nums]
        final = [x.count('1') for x in bnum]
        return final
'''

'''
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]
        while len(res) <= num:
            res = res + [x+1 for x in res]
        return res[:num+1]
'''