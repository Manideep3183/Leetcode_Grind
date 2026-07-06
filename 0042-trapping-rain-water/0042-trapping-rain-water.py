class Solution(object):
    def trap(self, height):
        if not height:
            return 0
        left, right = 0, len(height) - 1
        leftmax, rightmax = height[left], height[right]
        water = 0
        while left < right:
            if leftmax<rightmax:
                left+=1
                leftmax=max(leftmax,height[left])
                water+=leftmax-height[left]
            else:
                right-=1
                rightmax=max(rightmax,height[right])
                water+=rightmax-height[right]
        return water