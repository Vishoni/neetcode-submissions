class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        col = [set() for _  in range(9)]
        box = [set() for _ in range(9)]
        valid = True 
        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value ==".":
                     continue
                cell = ((r//3)*3)+(c//3)

                if value in rows[r] or value in col[c] or value in box[cell]:
                    valid = False 
                    break
                rows[r].add(value)
                col[c].add(value)
                box[cell].add(value)
            if not valid:
                break 
        return valid



        