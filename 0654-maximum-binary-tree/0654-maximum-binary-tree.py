# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        def build(l,r):
            if l > r:
                return None
            max_ind = l 
            for i in range(l+1, r+1):
                if nums[i] > nums[max_ind]:
                    max_ind = i
            root = TreeNode(nums[max_ind])
            root.left = build(l,max_ind-1)
            root.right = build(max_ind+1,r)
            return root
        return build(0,len(nums)-1)

