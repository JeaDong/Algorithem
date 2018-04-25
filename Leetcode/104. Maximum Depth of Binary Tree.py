#104. Maximum Depth of Binary Tree
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        if root:
            result = [root]
        else:
            result = []
        
        while result:
            depth += 1
            queue = []
            for node in result:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result = queue
        return depth
		
#递归
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1