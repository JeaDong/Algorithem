#108. Convert Sorted Array to Binary Search Tree
class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def travel(left,right):
            if left > right:
                return None
            mid = (left+right)//2
            node = TreeNode(nums[mid])
            node.left = travel(left,mid-1)
            node.right = travel(mid+1,right)
            return node
        return travel(0,len(nums)-1)