class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        next_greater = {}

        i = len(nums2) - 1

        while i >= 0:
            while stack and stack[-1] <= nums2[i]:
                stack.pop()

            if not stack:
                next_greater[nums2[i]] = -1
            else:
                next_greater[nums2[i]] = stack[-1]

            stack.append(nums2[i])
            i -= 1

        ans = []

        for num in nums1:
            ans.append(next_greater[num])

        return ans
        
        