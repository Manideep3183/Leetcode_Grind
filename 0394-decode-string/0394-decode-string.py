class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        curr_str = ''
        curr_num = 0
        for ch in s:
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)
            elif ch == '[':
                st.append((curr_num,curr_str))
                curr_num = 0
                curr_str = ''
            elif ch == ']':
                num, prev_str = st.pop()
                curr_str = prev_str + curr_str * num
            else:
                curr_str += ch
        return curr_str
