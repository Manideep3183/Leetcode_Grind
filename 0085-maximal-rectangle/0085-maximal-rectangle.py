class Solution(object):
    def maximalRectangle(self, matrix):
        def largestRectangle(height):
            st = []
            height.append(0)
            n = len(height)
            maxArea = 0
            for i in range(n):
                while st and height[st[-1]] > height[i]:
                    nse = i
                    ele = st[-1]
                    st.pop()
                    pse = st[-1] if st else -1
                    maxArea = max(maxArea, (nse-pse-1) * height[ele])
                st.append(i)
            height.pop()
            return maxArea
        m = len(matrix)
        n = len(matrix[0])
        maxRect = 0
        height = [0]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            maxRect = max(maxRect, largestRectangle(height))
        return maxRect

