class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        s = self.d[key]
        l = 0
        r = len(s)
        prev = ""
        while l < r:
            m = (l + r - 1) // 2
            if timestamp == s[m][0]:
                return s[m][1]
            elif timestamp > s[m][0]:
                prev = s[m][1]
                l = m + 1
            else:
                r = m
        
        return prev

