class Solution(object):
    def predictTheWinner(self, nums):
        memo = {}

        def get_max_diff(left, right):
            if left == right:
                return nums[left]
            
            if (left, right) in memo:
                return memo[(left, right)]

            # Choice 1: Take left element
            take_left = nums[left] - get_max_diff(left + 1, right)
            
            # Choice 2: Take right element
            take_right = nums[right] - get_max_diff(left, right - 1)

            memo[(left, right)] = max(take_left, take_right)
            return memo[(left, right)]

        # Player 1 wins if the relative score difference is >= 0
        return get_max_diff(0, len(nums) - 1) >= 0