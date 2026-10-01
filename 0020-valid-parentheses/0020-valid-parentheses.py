class Solution:
    def isValid(self, s: str) -> bool:
        st, mp = [], {')':'(', '}':'{', ']':'['}
        for c in s:
            if c in mp:
                if not st or st.pop() != mp[c]: return False
            else: st.append(c)
        return not st
