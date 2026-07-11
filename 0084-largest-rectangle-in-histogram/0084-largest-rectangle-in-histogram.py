class Solution(object):
    def largestRectangleArea(self, heights):
        heights.append(0)
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
        return maxArea