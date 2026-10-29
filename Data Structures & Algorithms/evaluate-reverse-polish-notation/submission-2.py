class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for token in tokens:
            if token in '-+*/':
                second = st.pop() if st else 0
                first  = st.pop() if st else 0
                if token == '+':
                    st.append(first + second)
                elif token == '-':
                    st.append(first - second)
                elif token == '*':
                    st.append(first * second)
                else:
                    st.append(int(first /second))
            else:
                st.append(int(token))
    
        return st[-1]