#递归解法
class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        s_string = self.travel(s)
        t_string = self.travel(t)
        return t_string in s_string
    def travel(self,node):
        if node:
            return '#' + str(node.val) + self.travel(node.left) + self.travel(node.right)
        else:
            return '?'
#迭代解法			
class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        
        def travel(node):
            result = [node]
            string = ''
            while result:
                cur = result.pop()
                if cur:
                    string += '#' + str(cur.val)
                    result.extend((cur.left,cur.right))
                else:
                    string += '?'
                
            return string
        s_string = travel(s)
        t_string = travel(t)
        return t_string in s_string