257. Binary Tree Paths

class Solution:
    def binaryTreePaths(self, root):
        if not root:#if rott is None: return []
            return []
        result,stack = [],[(root,'')]#we need to use 2 element to save the val and linked list
        while stack:#branch first search
            node,ls = stack.pop()
            if not node.left and not node.right:#it means the node is the node,
                result.append(ls+str(node.val))#then add in the result
            if node.right:
                stack.append((node.right,ls+str(node.val)+'->'))
            if node.left:
                stack.append((node.left,ls+str(node.val)+'->'))
        return result
###################		
def binaryTreePaths(self, root):
        
        if not root:
            return []
        result,queue = [],collections.deque([(root,'')])
        while queue:
            node,ls = queue.popleft()
            if not node.left and not node.right:
                result.append(ls+str(node.val))
            if node.left:
                queue.append((node.left,ls+str(node.val)+'->'))
            if node.right:
                queue.append((node.right,ls+str(node.val)+'->'))
        return result
####################
def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        self.travel(root,'',res)
        return res
    def travel(self,node,ls,res):
        #string += str(node.val)
        if node.left:
            self.travel(node.left,ls+str(node.val)+'->',res)
        if node.right:
            self.travel(node.right,ls+str(node.val)+'->',res)
        if not node.left and not node.right:
            res.append(ls+str(node.val))