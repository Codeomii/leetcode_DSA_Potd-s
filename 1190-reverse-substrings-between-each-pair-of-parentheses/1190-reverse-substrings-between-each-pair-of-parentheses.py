class Solution:
    def reverseParentheses(self, s):
        st = []
        for c in s:
            if c == ')':
                x = []
                while st[-1] != '(':
                    x.append(st.pop())
                st.pop()
                st.extend(x)
            else:
                st.append(c)
        return ''.join(st)