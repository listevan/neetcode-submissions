class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # search for correct row
        row = -1
        t = 0
        b = len(matrix)

        while t < b:
            m = (t+b-1) // 2
            if target > matrix[m][-1]:
                t = m+1
            elif target < matrix[m][-1]:
                if target > matrix[m][0]:
                    row = m
                    break
                elif target < matrix[m][0]:
                    b = m
                else:
                    return True
            else:
                return True

        # search for correct col
        if row == -1:
            return False
        l = 0
        r = len(matrix[row]) 

        while l < r:
            m = (l+r-1)//2
            if target > matrix[row][m]:
                l = m+1
            elif target < matrix[row][m]:
                r = m
            else:
                return True
        
        return False
        