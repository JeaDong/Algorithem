class Solution:
    def hasPathSum(self, root, sum):
        
        if not root:#
            return False
        stack = [(root,root.val)]
        while stack:
            node,node.val = stack.pop()
            if not node.left and not node.right:#意味着已经是在最底部了
                if node.val == sum:
                    return True
            if node.left:#第二个参数在每一次迭代过程中都添加节点的值
                stack.append((node.left,node.val+node.left.val))
            if node.right:
                stack.append((node.right,node.val+node.right.val))
        return False