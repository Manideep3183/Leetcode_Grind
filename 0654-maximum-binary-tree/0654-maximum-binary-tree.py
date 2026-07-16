# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return None
        max_ind = nums.index(max(nums))
        root = TreeNode(nums[max_ind])
        root.left = self.constructMaximumBinaryTree(nums[:max_ind])
        root.right = self.constructMaximumBinaryTree(nums[max_ind+1:])
        return root

