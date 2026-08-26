class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = []
        nge = {}
        for num in nums2[::-1]:
            while st and st[-1] <= num:
                st.pop()
            if not st:
                nge[num] = -1
            else:
                nge[num] = st[-1]
            st.append(num)
        return [nge[num] for num in nums1]    

        
        