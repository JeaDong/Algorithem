class Solution:
    def minDepth(self, root):
        #根据题意找到小最深度
        if not root:
            return 0
        result = [root]
        depth = 0
        min_dep = []
        while result:
            depth += 1
            queue = []
            for i in result:
                if not i.left and not i.right:#如果左右子节点都为None，证明到底部了，返回深度值
                    min_dep.append(depth)
                if i.left:
                    queue.append(i.left)
                if i.right:
                    queue.append(i.right)
            result = queue
        return min(min_dep)#最后返回最小的深度值
		
