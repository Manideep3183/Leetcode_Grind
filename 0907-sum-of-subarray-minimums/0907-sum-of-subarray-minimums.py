class Solution(object):
    def sumSubarrayMins(self, arr):
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
        nse = NSE(arr)
        pse = PSEE(arr)
        min_total = 0
        for i in range(len(arr)):
            left = i - pse[i]
            right = nse[i] - i
            min_total = (min_total + (left * right * arr[i])) 
        return min_total % (10**9+7)


            