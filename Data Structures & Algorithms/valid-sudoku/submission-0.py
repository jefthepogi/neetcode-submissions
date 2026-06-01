class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        grids = [{} for _ in range(9)]
        cols = {}
        for i, row in enumerate(board):
            rows = {}
            for j, col in enumerate(row):
                gridIndex = (i // 3) * 3 + (j // 3)
                if col == ".":
                    continue
                if col in rows:
                    return False
                hashdex = "".join([str(j), str(col)])
                if hashdex in cols:
                    return False
                if col in grids[gridIndex]:
                    return False
                rows[col] = 1
                cols[hashdex] = 1
                grids[gridIndex][col] = 1



        return True