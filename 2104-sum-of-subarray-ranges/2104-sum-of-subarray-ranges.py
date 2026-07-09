class Solution(object):
    def subArrayRanges(self, arr):
        def NSE(arr):
            n = len(arr)
            nse = [0] * n
            stack = []
            for i in range(n-1,-1,-1):
                while stack and arr[stack[-1]] > arr[i]:
                    stack.pop()
                nse[i] = n if not stack else stack[-1]
                stack.append(i)
            return nse
        def PSEE(arr):
            n = len(arr)
            pse = [0] * n
            stack = []
            for i in range(n):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                pse[i] = -1 if not stack else stack[-1]
                stack.append(i)
            return pse
        
        def NGE(arr):
            n = len(arr)
            nge = [0] * n
            stack = []
            for i in range(n-1,-1,-1):
                while stack and arr[stack[-1]] < arr[i]:
                    stack.pop()
                nge[i] = n if not stack else stack[-1]
                stack.append(i)
            return nge
        def PGEE(arr):
            n = len(arr)
            pge = [0] * n
            stack = []
            for i in range(n):
                while stack and arr[stack[-1]] <= arr[i]:
                    stack.pop()
                pge[i] = -1 if not stack else stack[-1]
                stack.append(i)
            return pge
        
        nse = NSE(arr)
        pse = PSEE(arr)
        min_total = 0
        for i in range(len(arr)):
            left = i - pse[i]
            right = nse[i] - i
            min_total = (min_total + (left * right * arr[i])) 
        
        nge = NGE(arr)
        pge = PGEE(arr)
        max_total = 0
        for i in range(len(arr)):
            left = i - pge[i]
            right = nge[i] - i
            max_total = (max_total + (left * right * arr[i]))

        return max_total - min_total