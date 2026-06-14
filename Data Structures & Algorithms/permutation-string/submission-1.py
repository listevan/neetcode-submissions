class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_chars = [0]*26
        s2_chars = [0]*26
        for i in range(len(s1)):
            s1_chars[ord(s1[i])-ord("a")] += 1
            s2_chars[ord(s2[i])-ord("a")] += 1
        # print(f"s1: {s1_chars}")
        # print(f"s2: {s2_chars}")
        
        if s1_chars == s2_chars:
            return True
        
        for i in range(1, len(s2)-len(s1)+1):
            s2_chars[ord(s2[i-1])-ord("a")] -= 1
            s2_chars[ord(s2[i+len(s1)-1])-ord("a")] += 1
            # print(f"s2: {s2_chars}")
            if s1_chars == s2_chars:
                return True

        return False