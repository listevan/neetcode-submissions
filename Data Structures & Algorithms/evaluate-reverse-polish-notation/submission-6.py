class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        while tokens:
            print(s, tokens)
            val = tokens.pop(0)
            if val.isdigit() or (val[0] == "-" and len(val) > 1):
                s.append(int(val))
            else:
                r = s.pop()
                l = s.pop()
                if val == "+":
                    l = l + r
                elif val == "-":
                    l = l - r
                elif val == "*":
                    l = l * r
                else:
                    l = int(l/r)
                s.append(l)
        return s.pop()
