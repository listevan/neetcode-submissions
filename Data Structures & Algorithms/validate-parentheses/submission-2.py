class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for ss in s:
            if ss == "[" or ss == "{" or ss == "(":
                st.append(ss)
            else:
                if not st:
                    return False
                sm = st.pop(-1)
                if sm == "[" and ss != "]":
                    return False
                if sm == "{" and ss != "}":
                    return False
                if sm == "(" and ss != ")":
                    return False
        return not st