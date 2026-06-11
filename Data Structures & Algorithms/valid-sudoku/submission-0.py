class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        box = [[[False,False,False] for i in range(n)] for j in range(n)]

        for i in range(n):
            for j in range(n):
                box_ind = i//3 * 3 + j//3
                curr_val = board[i][j]
                if not curr_val.isdigit():
                    continue
                curr_val = int(curr_val) - 1

                if box[i][curr_val][0] or box[j][curr_val][1] or box[box_ind][curr_val][2]:
                    return False
                else:
                    box[i][curr_val][0] = True
                    box[j][curr_val][1] = True
                    box[box_ind][curr_val][2] = True

    
        return True