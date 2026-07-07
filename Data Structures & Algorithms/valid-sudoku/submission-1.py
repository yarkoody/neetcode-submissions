class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        blocks = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                el = board[r][c]
                if el == '.':
                    continue
                if el in rows[r] or el in cols[c] or el in blocks[(r // 3, c // 3)]:
                    return False
                rows[r].add(el)
                cols[c].add(el)
                blocks[(r//3, c//3)].add(el)
        return True

                
        