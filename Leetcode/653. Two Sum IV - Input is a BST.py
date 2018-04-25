#653. Two Sum IV - Input is a BST
class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if root:
            result = [root]
        else:
            return False
        aset = set()
        while result:
            cur = result.pop(0)
            if k-cur.val in aset:
                return True
            aset.add(cur.val)
            if cur.left:
                result.append(cur.left)
            if cur.right:
                result.append(cur.right)
        return False
#递归
class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.f = False
        aset = set()
        def travel(root):
            if not root:
                return 
            if k-root.val not in aset:
                aset.add(root.val)
            else:
                self.f = True
            travel(root.left)
            travel(root.right)
        travel(root)
        return self.f