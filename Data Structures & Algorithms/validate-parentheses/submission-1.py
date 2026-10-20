class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {'}' : '{', ')': '(', ']': '['}
        st = []
        for ch in s:
            if ch in parentheses:
                par = st.pop() if st else ""
                if parentheses[ch] != par:
                    return False
            else:
                st.append(ch)

        return not st