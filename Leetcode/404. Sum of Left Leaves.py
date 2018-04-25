# 404. Sum of Left Leaves

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            result = [root]
        else:
            return 0
        LeftSum = 0
        while result:
            cur = result.pop()
            if cur.left:
                if not cur.left.left and not cur.left.right:
                    LeftSum += cur.left.val
                result.append(cur.left)
            if cur.right:
                result.append(cur.right)
        return LeftSum