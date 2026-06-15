class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sz = sorted(zip(position, speed), reverse=True)

        time = []
        for p, s in sz:
            time.append((target-p) / s)
        # print(time)
        
        i = 0
        res = 0
        while i < len(time):
            # print(i)
            res += 1
            j = i
            while i+1 < len(time) and time[i+1] <= time[j]:
                i+=1
            i += 1
        
        return res