class Solution:
    def isValid(self, s: str) -> bool:
        st =[]
        pars = {')':'(', ']':'[','}':'{'} 
        for ch in s:
            if ch not in pars:
                st.append(ch)
            elif ch in pars:
                if not st or st[-1] != pars[ch]:
                    return False
                st.pop()

        if st :
            return False
        return True