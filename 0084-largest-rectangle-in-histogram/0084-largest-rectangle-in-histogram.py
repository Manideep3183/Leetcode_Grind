class Solution(object):
    def largestRectangleArea(self, heights):
        n = len(heights)
        maxArea = 0
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                ele = stack[-1]
                stack.pop()
                nse = i
                pse = stack[-1] if stack else -1
                maxArea = max(maxArea, heights[ele] * (nse - pse - 1))
            stack.append(i)
        while stack:
            ele = stack[-1]
            stack.pop()
            nse = n
            pse = stack[-1] if stack else -1
            maxArea = max(maxArea, heights[ele] * (nse - pse - 1))
        return maxArea