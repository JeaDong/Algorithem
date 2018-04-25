#637. Average of Levels in Binary Tree
#递归
lass Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """#这段代码我觉得写得优雅，可是学不来
        result = []#for save the value and numbers of childnode
        def dfs(node,depth=0):
            if node:
                if len(result) <= depth:
                    result.append([0,0])
                result[depth][0] += node.val
                result[depth][1] += 1
                dfs(node.left,depth+1)
                dfs(node.right,depth+1)
        dfs(root)
        return [i/j for i,j in result]
#迭代		
class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        result = [root]
        fina = []
        while result:
            total = 0
            num = 0
            queue = []
            while result:
                cur = result.pop()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                total += cur.val
                num += 1
            result = queue
            fina.append(total/num)
        return fina